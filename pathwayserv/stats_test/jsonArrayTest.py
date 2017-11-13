import json;
import numpy as np;
from geopy.distance import vincenty;


speedList = [];
distList = [];
distAccum = 0;
dbJson = json.load(open("sampleJson.json"));#pretending this is from the runs table and has been filtered to show all of a user's runs
runCount = 0; 
routeCount = 0;# will calc this by pulling data either from the user's route or from the route table and filtering it manually

# run calcs over run data
for idxJson in range(0,len(dbJson)):
     #print(dbJson[idxJson]);
     tempListSpd = [];
     sub = dbJson[idxJson];
     totaltime_r = sub["timestamps"][len(sub["timestamps"])-1];
     for idx in range (0, len(sub)-1):
          
          dist = round((vincenty(tuple(sub["coordinates"][idx])[1::-1], tuple(sub["coordinates"][idx+1])[1::-1]).miles), 3); #[1::-1] used to reversed to allow
          distAccum = round(distAccum + dist, 3);
          spdTmp = (dist)/(sub["timestamps"][idx+1] - sub["timestamps"][idx]);
          tempListSpd.append(spdTmp);

     speedList.append(np.max(tempListSpd));
     distList.append(distAccum);

print ("max speed:", speedList);
print (distList);
print (distAccum);


