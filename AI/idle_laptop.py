import psutil
import time
import screen_brightness_control as sbc
from plyer import notification
from pynput.mouse import Controller as MouseController


IDLE_THRESHOLD_PERCENT = 5
RAM_THRESHOLD_PERCENT = 55
DURATION = 2
IDLE_DURATION_THRESHOLD = 300 

def is_cursor_moving():
    mouse = MouseController()
    current_position = mouse.position
    time.sleep(10) 
    new_position = mouse.position
    return current_position != new_position

def is_system_idle_state():
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)
    avg_cpu_percent = sum(cpu_percentages) / len(cpu_percentages)
    ram_percent = psutil.virtual_memory().percent
    return avg_cpu_percent < IDLE_THRESHOLD_PERCENT and \
           ram_percent < RAM_THRESHOLD_PERCENT and \
           not is_cursor_moving()

def notify(title, message):
    notification.notify(title=title, message=message, app_icon=None, timeout=10)

def adjust_brightness(level):
    try:
        sbc.set_brightness(level)
    except Exception as e:
        print(f"Failed to adjust brightness: {e}")

def sleep_system():
    try:
        import ctypes
        ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
    except OSError as e:
        print(f"Failed to sleep the system: {e}")

def main():
    idle_duration_counter = 0
    is_idle = False

    while True:
        if is_system_idle_state():
            if not is_idle:
                adjust_brightness(30)
                notify('System Idle Notification', 'System is now idle. Screen brightness reduced by 30%.')
                is_idle = True
            idle_duration_counter += DURATION
            if idle_duration_counter >= IDLE_DURATION_THRESHOLD:
                print("System idle for too long. Putting the system to sleep mode.")
                sleep_system()
        else:
            if is_idle:
                adjust_brightness(50)
                notify('System Active Notification', 'System is no longer idle. Screen brightness set back to 50%.')
                is_idle = False
            idle_duration_counter = 0
        time.sleep(DURATION)

if __name__ == "__main__":
    main()
