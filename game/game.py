"""
Text-Based Adventure Game

A simple text adventure game with:
- Player class with inventory, health, and score
- Multiple locations with unique events
- Random encounters (monsters, loot, allies)
- Combat mechanics with consequences

Run: python game.py
Commands: explore, status, inventory, help, quit
"""

import random


class Player:
    """Represents the game player with inventory, health, and score."""
    
    def __init__(self, name):
        """Initialize player with starting stats."""
        self.name = name
        self.health = 100
        self.max_health = 100
        self.score = 0
        self.inventory = []
        self.location = "Starting Village"
    
    def add_item(self, item):
        """Add item to inventory."""
        self.inventory.append(item)
        print(f"✓ Added {item}!")
    
    def remove_item(self, item):
        """Remove item from inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def take_damage(self, damage):
        """Reduce health by damage amount."""
        self.health = max(0, self.health - damage)
        print(f"💔 Took {damage} damage! Health: {self.health}/{self.max_health}")
    
    def heal(self, amount):
        """Increase health by amount."""
        self.health = min(self.max_health, self.health + amount)
        print(f"💚 Healed {amount}! Health: {self.health}/{self.max_health}")
    
    def add_score(self, points):
        """Add points to score (can be negative)."""
        self.score += points
        sign = "+" if points > 0 else ""
        print(f"⭐ {sign}{points} points! Total: {self.score}")
    
    def show_status(self):
        """Display player stats."""
        bar = '█' * (self.health // 10) + '░' * (10 - self.health // 10)
        print(f"\n{'='*40}")
        print(f"📊 {self.name}'s Status")
        print(f"{'='*40}")
        print(f"Location: {self.location}")
        print(f"Health: {self.health}/{self.max_health} {bar}")
        print(f"Score: {self.score}")
        items = ", ".join(self.inventory) if self.inventory else "Empty"
        print(f"Inventory: {items}")
        print(f"{'='*40}\n")
    
    def is_alive(self):
        """Check if player is alive."""
        return self.health > 0


class Game:
    """Main game controller."""
    
    # Game locations with descriptions
    LOCATIONS = {
        "Dark Forest": "A misty forest with ancient trees looming overhead.",
        "Mystical Cave": "A glowing cave with strange symbols on the walls.",
        "Village Square": "A bustling village with merchants calling out.",
        "Enchanted Castle": "A magnificent glowing castle with inviting doors."
    }
    
    # Monsters with damage and points
    MONSTERS = [
        {"name": "Goblin", "damage": 10, "points": 15},
        {"name": "Orc", "damage": 20, "points": 25},
        {"name": "Dragon", "damage": 35, "points": 50},
        {"name": "Troll", "damage": 15, "points": 20},
    ]
    
    # Loot with values
    LOOT = [
        {"name": "Gold Coin", "value": 5},
        {"name": "Silver Dagger", "value": 20},
        {"name": "Magic Potion", "value": 15},
        {"name": "Legendary Sword", "value": 50},
    ]
    
    def __init__(self, player_name):
        """Initialize game with player."""
        self.player = Player(player_name)
        self.running = True
        self.commands = ["explore", "status", "inventory", "help", "quit"]
    
    def explore(self):
        """Handle explore command - visit a random location."""
        if not self.player.is_alive():
            print("💀 You are defeated. Game Over!")
            self.running = False
            return
        
        # Pick random location
        location = random.choice(list(self.LOCATIONS.keys()))
        self.player.location = location
        print(f"\n📍 {location}")
        print(f"{self.LOCATIONS[location]}\n")
        
        # Random encounter type
        encounter = random.choice(["monster", "loot", "ally"])
        
        if encounter == "monster":
            self._fight_monster()
        elif encounter == "loot":
            self._find_loot()
        else:
            self._meet_ally()
    
    def _fight_monster(self):
        """Handle combat encounter."""
        monster = random.choice(self.MONSTERS)
        print(f"⚔️  A {monster['name']} appears!")
        action = input("Do you [fight] or [run]? ").strip().lower()
        
        if action == "fight":
            self.player.take_damage(monster["damage"])
            self.player.add_score(monster["points"])
            print(f"✓ Defeated the {monster['name']}!")
            
            # 50% chance for loot
            if random.random() > 0.5:
                loot = random.choice(self.LOOT)
                self.player.add_item(loot["name"])
                self.player.add_score(loot["value"])
        
        elif action == "run":
            print("You fled in panic! Lost treasure opportunity.")
            self.player.add_score(-10)
        
        else:
            print("You hesitated. The creature vanished.")
            self.player.add_score(-5)
        print()
    
    def _find_loot(self):
        """Handle treasure encounter."""
        loot = random.choice(self.LOOT)
        print(f"🎁 You found a {loot['name']}!")
        self.player.add_item(loot["name"])
        self.player.add_score(loot["value"])
        print()
    
    def _meet_ally(self):
        """Handle ally encounter."""
        print("🤝 A friendly traveler helps you!")
        self.player.heal(20)
        self.player.add_score(10)
        print()
    
    def show_inventory(self):
        """Display inventory."""
        print("\n🎒 Inventory:")
        if self.player.inventory:
            for i, item in enumerate(self.player.inventory, 1):
                print(f"  {i}. {item}")
        else:
            print("  (empty)")
        print()
    
    def show_help(self):
        """Display available commands."""
        print(f"\n{'='*40}")
        print("📖 Commands")
        print(f"{'='*40}")
        print("  explore   - Explore a random location")
        print("  status    - Show your stats")
        print("  inventory - View your items")
        print("  help      - Show this message")
        print("  quit      - Exit game")
        print(f"{'='*40}\n")
    
    def handle_command(self, command):
        """Process player command."""
        command = command.strip().lower()
        
        if command == "explore":
            self.explore()
        elif command == "status":
            self.player.show_status()
        elif command == "inventory":
            self.show_inventory()
        elif command == "help":
            self.show_help()
        elif command == "quit":
            print(f"Thanks for playing! Final Score: {self.player.score}\n")
            self.running = False
        else:
            print(f"Unknown command: '{command}'. Try: {', '.join(self.commands)}\n")
    
    def run(self):
        """Main game loop."""
        print(f"\n{'='*40}")
        print(f"⚔️  Welcome, {self.player.name}!")
        print(f"{'='*40}")
        print("Your adventure begins. Type 'help' for commands.\n")
        
        while self.running and self.player.is_alive():
            try:
                cmd = input("> ").strip()
                if cmd:
                    self.handle_command(cmd)
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Goodbye!")
                break
        
        if not self.player.is_alive():
            print(f"\n💀 Game Over! Final Score: {self.player.score}\n")


def main():
    """Entry point."""
    name = input("Enter your name, adventurer: ").strip() or "Unknown Hero"
    game = Game(name)
    game.run()


if __name__ == "__main__":
    main()
