# Importing necessary libraries from WarThunder for telemetry and map information, pprint for formatted output,
# csv for CSV file operations, os for operating system interactions, and time for time-related functions.
from WarThunder import telemetry
from WarThunder import mapinfo
from pprint import pprint
import csv
import os
import time

# Initialize a boolean flag to track if the timer has started.
isTimerStarted : bool = False

# Define a function to print basic telemetry data in a formatted manner.
def find_basic_telemetry():
    print('------------------------------------------------------')
    print('Basic Telemetry:')
    # Pretty print the basic telemetry data
    pprint(telem.basic_telemetry)
    print('')

# Open (or create if not present) a CSV file for appending data.
f = open('/home/user/data/write.csv','a')
# Create a CSV writer object to write data into the CSV file.
wr = csv.writer(f)

try:
    # Start an infinite loop to continuously gather telemetry data.
    while True:
        # Initialize the telemetry interface.
        telem = telemetry.TelemInterface()
            
        # Wait in this loop until telemetry data becomes available.
        while not telem.get_telemetry():
            pass

        # Start the timer once when the telemetry data is first available.
        if not isTimerStarted:
            isTimerStarted=True
            initTime = time.time()
        
        # Calculate the time passed since the timer started.
        timePassed = time.time() - initTime

        # Extract latitude, longitude, and altitude data from the telemetry.
        lat=telem.basic_telemetry['lat']
        lon=telem.basic_telemetry['lon']
        alt=telem.basic_telemetry['altitude']

        # Write the timestamp and telemetry data to the CSV file.
        wr.writerow([initTime,lat,lon,alt])
        # Call the function to print the basic telemetry data.
        find_basic_telemetry()

        # Sleep for 0.1 seconds before collecting the next set of data.
        time.sleep(0.1)
# Handle the case where the script is interrupted manually.
except KeyboardInterrupt:
    print('interrupted!')
    # Close the CSV file properly to ensure data is saved.
    f.close()