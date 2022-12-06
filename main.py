from boltiot import Bolt
import json, time
api_key = "b1ddb51c-9c25-488e-984a-410b12ee53dd"
device_id  = "BOLT9047996"
minimum_limit = 300
maximum_limit = 450
mybolt = Bolt(api_key,device_id)
while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    temp1 = (int(float(data['value']))*100)/1024
    print("Sensor value is: " ,float(temp1))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
           print(mybolt.digitalWrite('0','HIGH'))
        else:
           print(mybolt.digitalWrite('0','LOW'))
    except Exception as e: 
         print ("Error occured: Below are the details")
         print(e)
    time.sleep(10)    
