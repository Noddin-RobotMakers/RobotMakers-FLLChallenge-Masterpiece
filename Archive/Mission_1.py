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
TURN_RATE = 300
TURN_ACC = 1000


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


# Solve mission 1
# ---------------
def solve_and_return_to_base():
    # Settings for drivebase
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)
    # Drive forward
    drivebase.straight(distance=100, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=80, then=Stop.HOLD, wait=True)
    # Turn back
    drivebase.turn(angle=-80, then=Stop.HOLD, wait=True)
    # Return to base
    drivebase.straight(distance=-300, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_and_return_to_base()
