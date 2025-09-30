class smart_home:
    def __init__(self, temperature, security_status, lights_status):
        self.temperature = temperature
        self.security_status = security_status
        self.lights_status = lights_status
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature set to {self.temperature}°F")

    def toggle_security(self):
        self.security_status = not self.security_status
        status = "armed" if self.security_status else "disarmed"
        print(f"Security system is now {status}")   

    def toggle_lights(self):
        self.lights_status = not self.lights_status
        status = "on" if self.lights_status else "off"
        print(f"Lights are now {status}")

# Example usage
home = smart_home(22, False, False)
home.set_temperature(70)
home.toggle_security()
home.toggle_lights()
