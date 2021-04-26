import rpc
import time
from time import mktime

print("")  # Application's Name + Something like "loading..."
client_id = ""  # Your application's client ID
rpc_obj = rpc.DiscordIpcClient.for_platform(
    client_id)  # Send the client ID to the rpc module
# Needs to know if connection was successful leave this one alone
print("RPC connection successful")
timesince = 'Time elapsed:'
minute = 0
second = 0
time.sleep(0.5)  # Can make it longer or shorter if necessary
# -Year-Month-Day-Hour-Minute-Second-Unknown-Unknown-Unknown
t = (1, 2, 3, 4, 5, 6, 000, 000, 000)
end_time = mktime(t)
start_time = mktime(time.localtime())
# You can comment these out if wanted:
print("Eposh Time: %f" % end_time)
print("Date and Time: %s" % time.asctime(time.localtime(end_time)))
print("Main Connection Successful")
while True:
    activity = {
        "details": "",  # First Line
        "state": "",  # Second Line
        "timestamps": {
            "start": start_time,
            # To 'elapse' instead of 'left' comment the lower line out completely
            # "end": end_time
        },
        "assets": {
            "small_text": "Null",  # Main Tooltip, to ignore type 'Null'
            "small_image": "null",  # Main image name; to ignore type 'null'
            "large_text": "",  # Large Tooltip
            "large_image": ""  # Main image name
        }
    }

    rpc_obj.set_activity(activity)
    try:
        while True:
            if second == 59:
                minute += 1
                second -= 59
            else:
                second += 1
            time.sleep(1)
            print(timesince, minute, 'm', second, 's', '\b',
                  end='\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b', flush=True)
    except KeyboardInterrupt:
        print('\n')
        exit()
        # time.sleep(30) // Unsure if this actually needs to be here
