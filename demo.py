from airtouch3 import AirTouch3
from airtouch3 import AT3CommsStatus
from airtouch3 import AT3Command
from airtouch3.airtouch3 import AT3AcFanSpeed

at3 = AirTouch3('192.168.1.72')
at3.update_status()

if at3.comms_status != AT3CommsStatus.OK:
    print("Connection failed "+at3.comms_error)
    exit()
at3.print_status()

print(f"Fan Speed for AC0 {at3.set_fan_speed_ac_unit(1, AT3AcFanSpeed.HIGH)}")
exit()

# Toggle a zone on/off
#print(f"Toogle Group 7 {at3.groups[7].toggle()}")
print(f"Toogle Group 7 {at3.toggle_group(7)}")
at3.print_status()
g = at3.groups[7]
print(f"Group {g.name}: {g.is_on}; Mode is {g.mode}; {g.open_percent}%; "
     f"Temp: {g.temperature}degC Target: {g.temperature_sp}degC")

# Increase a group position
#print(f"Increase zone 0: {at3.toggle_position_group(0, AT3Command.INCREMENT)}")
print(f"Increase zone 0: {at3.groups[0].position_inc()}")
g = at3.groups[0]
print(f"Group {g.name}: {g.is_on}; Mode is {g.mode}; {g.open_percent}%; "
      f"Temp: {g.temperature}degC Target: {g.temperature_sp}degC")

# Decrease a group position
print(f"Decrease zone 6: {at3.toggle_position_group(6, AT3Command.DECREMENT)}")
#print(f"Decrease zone 6: {at3.groups[6].position_dec()}")
g = at3.groups[6]
print(f"Group {g.name}: {g.is_on}; Mode is {g.mode}; {g.open_percent}%; "
      f"Temp: {g.temperature}degC Target: {g.temperature_sp}degC")

# Toogle AC Unit 1 on/off
#print(f"Toogle AC Unit 1 {at3.toggle_ac_unit(1)}")
print(f"Toogle AC Unit 1 {at3.ac_units[1].toggle()}")

# Toogle AC Unit 1 Temp Setpoint Up
#print(f"Toogle AC Unit 1 {at3.toggle_temperature_ac_unit(1, AT3Command.INCREMENT)}")
print(f"Toogle AC Unit 1 {at3.ac_units[1].temperature_inc()}")

# Toogle AC Unit 0 Temp Setpoint Down
#print(f"Toogle AC Unit 0 {at3.toggle_temperature_ac_unit(0, AT3Command.DECREMENT)}")
print(f"Toogle AC Unit 0 {at3.ac_units[0].temperature_dec()}")

# Example responses:
#data = b'\xf2\xfa\x14\x11\x04\x02\x05\x1a\x85\x00\x88\x00\x85\x00\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x86\x1e\x88\x00\x91\x1e\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x86\x1e\x88\x00\x91\x1e\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x86\x1e\x88\x00\x91\x1e\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1eKitchen\x00Family\x00\x00Lydia   Steph   Lounge\x00\x00Dining\x00\x00Master\x00\x00Study\x00\x00\x00Group_9\x00Group_A\x00Group_B\x00Group_C\x00Group_D\x00Group_E\x00Group_F\x00Group_G\x00\x80\x89\x02\x03\x04\x05\x8e\x07\x80\x81\x82\x83\x84\x85\x86\x87\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x01\x11!1AQaq\x81\x91\xa1\xb1\xc1\xd1\xe1\xf1\n\x8a\n\n\x8a\n\n\n\n\n\n\n\n\n\n\n\x19\x18\x18\x189\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18Living  DAY\x00\x00\x00\x00\x00Fav_3   Fav_4\x00\x00\x00\xcc\x00\xcd\x00\x80\x00\x00\x00\x08\x84\x00\x02\x03\xe5#\x00\x00Polyaire\x00\x0008 8349 8466Polyaire\x00\x00\x00\x00\x00\x00\x00\x00TOP\x00\x00\x00\x00\x00BOTTOM\x00\x00\x85\x00\x86\x1e\x85\x00\x86\x1e\x00\x80\x00\x01\x04\x043"\x18\x17\x1d\x1d\x00\x00\x00\x00\x08\x08\x00\x00\x05\x00\x9a\x00\t\r\xa5\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0093051723+'
#data = b'\xf2\xfa\x14\x11\x04\x02\t\x00\x85\x00\x88\x00\x85\x00\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x86\x1e\x88\x00\x91\x1e\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x86\x1e\x88\x00\x91\x1e\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x86\x1e\x88\x00\x91\x1e\x96\x00\x87\x1e\x8c\x1e\x92\x00\x97\x1e\x87\x1e\x8c\x1e\x92\x00\x97\x1eKitchen\x00Family\x00\x00Lydia   Steph   Lounge\x00\x00Dining\x00\x00Master\x00\x00Study\x00\x00\x00Group_9\x00Group_A\x00Group_B\x00Group_C\x00Group_D\x00Group_E\x00Group_F\x00Group_G\x00\x80\x81\x02\x03\x04\x05\x86\x07\x80\x81\x82\x83\x84\x85\x86\x87\x13\x12\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x01\x11!1AQaq\x81\x91\xa1\xb1\xc1\xd1\xe1\xf1\x8a\n\n\n\n\n\x8a\n\n\n\n\n\n\n\n\n\x19\x18\x18\x189\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18Living  DAY\x00\x00\x00\x00\x00Fav_3   Fav_4\x00\x00\x00\xcc\x00\xcd\x00\x80\x00\x00\x00\x08\x84\x00\x00\x00\xe5#\x00\x00Polyaire\x00\x0008 8349 8466Polyaire\x00\x00\x00\x00\x00\x00\x00\x00TOP\x00\x00\x00\x00\x00BOTTOM\x00\x00\x85\x00\x86\x1e\x85\x00\x86\x1e\x00\x80\x00\x01\x04\x043"\x18\x19\x1b\x1b\x00\x00\x00\x00\x08\x08\x00\x00\x05\x00\x9a\x00\t\r\xa9\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0093051723\xff'