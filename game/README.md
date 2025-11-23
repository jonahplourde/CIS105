# Text-Based Adventure Game 🎮

A simple text adventure game with inventory, health, score, and random encounters.

## Quick Start

```bash
python game.py
```

Enter your name and start exploring!

## Features

✅ **Player Class**: Tracks name, health (max 100), score, and inventory  
✅ **Inventory System**: Add/remove items when fighting or finding loot  
✅ **Health/Points**: Health decreases in combat; points awarded for winning  
✅ **Combat**: Fight monsters (damage + points), run (-10 points), or hesitate (-5 points)  
✅ **4 Locations**: Dark Forest, Mystical Cave, Village Square, Enchanted Castle  
✅ **Random Events**: Encounter monsters, find treasure, or meet allies  
✅ **Status Command**: Check health, inventory, score, and location  

## Commands

| Command | Description |
|---------|-------------|
| `explore` | Visit a random location with encounters |
| `status` | Show player stats and health bar |
| `inventory` | List items collected |
| `help` | Display commands |
| `quit` | Exit game |

## Game Example

```
> explore

📍 Dark Forest
A misty forest with ancient trees looming overhead.

⚔️  A Goblin appears!
Do you [fight] or [run]? fight
💔 Took 10 damage! Health: 90/100
✓ Defeated the Goblin!
🎁 You found a Gold Coin!
✓ Added Gold Coin!

> status

========================================
📊 TestHero's Status
========================================
Location: Dark Forest
Health: 90/100 █████░░░░░
Score: 15
Inventory: Gold Coin
========================================
```

## Code Structure

### Player Class
Manages all player data and actions:

```python
player = Player("Aragorn")
player.add_item("Sword")        # Add to inventory
player.take_damage(10)           # Health decreases
player.add_score(50)             # Gain/lose points
player.heal(20)                  # Restore health
player.show_status()             # Display stats
```

### Game Class
Handles game logic and commands:
- `explore()`: Visit random locations
- `_fight_monster()`: Combat system
- `_find_loot()`: Treasure encounters
- `_meet_ally()`: Healing events
- `handle_command()`: Process player input
- `run()`: Main game loop

### Locations & Encounters
- **Monsters**: Deal damage, award points, drop loot
- **Loot**: Add items, give points
- **Allies**: Heal player, give bonus points

## Running Tests

```bash
python test_game.py
```

Tests cover:
- Player initialization and stats
- Inventory operations (add/remove)
- Damage and healing
- Score tracking
- Command processing
- Complete game scenarios

## How to Extend

### Add a New Location
Edit `Game.LOCATIONS`:
```python
"Dark Castle": "A creepy castle looms before you...",
```

### Add a New Monster
Edit `Game.MONSTERS`:
```python
{"name": "Vampire", "damage": 30, "points": 40},
```

### Add a New Item
Edit `Game.LOOT`:
```python
{"name": "Ancient Ring", "value": 75},
```

### Add a New Command
In `Game.handle_command()`:
```python
elif command == "save":
    self.save_game()
```

## Game Design

- **Modular**: Player class separate from Game logic
- **Clean Loop**: Simple command input and processing
- **Readable**: Inline comments explain features
- **Extensible**: Easy to add locations, items, monsters
- **Tested**: Unit tests verify core functionality

## Tips

- **Fight early** to build health and points
- **Watch your health** using the status command
- **Collect loot** to track your journey
- **Take calculated risks** - some defeats give experience!

---

Enjoy your adventure! ⚔️
