# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


# CONSTANTS
# =========
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 80
TURN_ACC = 85


# VARIABLE (HUB)
# ==============
hub = InventorHub()

# VARIABLES (DRIVING MOTORS + DRIVEBASE)
# ======================================
left_motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.C)
drivebase = DriveBase(left_motor, right_motor, 56, 110)

# VARIABLES (ATTACHMENT MOTORS)
# =============================
left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)

# VARIABLES (SENSORS)
# ===================
right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)


# FUNCTIONS
# =========

# Solve mission 6
# ---------------
def solve_mission_6():
    # Settings for drive
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)
    # Drive forward
    drivebase.straight(780)
    # Turn to face mission
    drivebase.turn(50)
    # Drive into mission
    drivebase.straight(210)
    # Do the speakers
    left_attachent_motor.run_angle(speed=1000, rotation_angle=-270,
                                   then=Stop.COAST, wait=True)
    # Turn
    drivebase.turn(-45)
    # Recoil the stick
    left_attachent_motor.run_angle(speed=1000, rotation_angle=180,
                                   then=Stop.COAST, wait=True)
    # Turn
    drivebase.turn(60)
    # Drive backwards
    drivebase.straight(-100)


# Return to base after completing the mission
# -------------------------------------------
def return_to_base():
    # Turn
    drivebase.turn(-90)
    # Drive towards home
    drivebase.straight(-300)
    # Turn
    drivebase.turn(-50)
    # Drive back to home
    drivebase.straight(-600)


# MAIN PROGRAM
# ============
solve_mission_6()
return_to_base()
