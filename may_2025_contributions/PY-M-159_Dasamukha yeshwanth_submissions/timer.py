import time
def countdown(seconds):
    print(f"\nStarting countdown for {seconds} seconds...\n")
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timeformat = f"{mins:02d}:{secs:02d}"
            print(f"Time Remaining: {timeformat}", end='\r')
            time.sleep(1)
            seconds -= 1
        print("\nTime's up! 🎉")
    except KeyboardInterrupt:
        print("\nCountdown cancelled by user.")

def stopwatch():
    print("\nStopwatch started. Press Ctrl+C to stop.\n")
    start_time = time.time()
    try:
        while True:
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            timeformat = f"{mins:02d}:{secs:02d}"
            print(f"Elapsed Time: {timeformat}", end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nStopwatch stopped at {timeformat}.")

def main():
    print("Welcome to the Simple Stopwatch/Timer!")
    print("Choose an option:")
    print("1. Countdown Timer")
    print("2. Stopwatch")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == '1':
        while True:
            duration_input = input("Enter countdown duration in seconds: ").strip()
            if duration_input.isdigit() and int(duration_input) > 0:
                countdown(int(duration_input))
                break
            else:
                print("Please enter a valid positive number.")
    elif choice == '2':
        stopwatch()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()