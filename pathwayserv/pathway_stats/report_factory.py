from . import report as rep;
import json;
import numpy as np;
import statistics as stats;
from geopy.distance import vincenty;

class ReportFactory:


    def doUserReport(self, uid, rid):
        """ Retrieve relevant records for all routes from user's"""
        print("");


    """

    """
    def doBasicReport(self, uid, rid):
        """Retrieve relevant record for the specific route: most recent run and best run"""


        """Retrieve user's physical profile data"""





        speedList_r = [];
        distList_r = [0];
        distAccum_r = 0;

        """Gather user profile info age, weight, gender"""
        age = 28;
        weight = 150;
        heart_rate = 208 - (0.7 * age);
        gender = 'male';
        calories_burned = 0;

        """ this is called to read in json from a string"""
        #myJson = json.loads("""Recent Run goes here""");
        myJson = json.load(open("sampleJson.json"));

        """ Determine Distance and speed from coordinates for recent run """
        #path to the coordinates in a standard geojson structure
        sub = myJson["coordinates"];
        totaltime_r = myJson["timestamps"][len(myJson["timestamps"])-1];
        for idx in range (0, len(sub)-1):
            dist = round((vincenty(tuple(sub[idx])[1::-1], tuple(sub[idx+1])[1::-1]).miles), 3); #[1::-1] used to reversed to allow
            distList_r.append(dist);
            spdTmp = (distList_r[len(distList_r) - 1])/(myJson["timestamps"][idx+1] - myJson["timestamps"][idx]);
            speedList_r.append(round(spdTmp, 3));

        """------------------------------------------------------------"""
        """------------------------------------------------------------"""
        """------------------------------------------------------------"""
        """ Determine Distance and speed from coordinates for best run """
        speedList_b = [];
        distList_b = [0];
        distAccum_b = 0;
        #myJson = json.loads("""Best Run goes here""");
        myJson = json.load(open("sampleJson2.json"));

        #path to the coordinates in a standard geojson structure
        sub = myJson["coordinates"];
        totaltime_b = myJson["timestamps"][len(myJson["timestamps"])-1];
        for idx in range (0, len(sub)-1):
            dist = round((vincenty(tuple(sub[idx])[1::-1], tuple(sub[idx+1])[1::-1]).miles), 3);
            distList_b.append(dist);
            spdTmp = (distList_b[len(distList_b) - 1])/(myJson["timestamps"][idx+1] - myJson["timestamps"][idx]);
            speedList_b.append(round((spdTmp), 3));

        if gender == "male":
            calories_burned = ((-55.0969 + (0.6309 * heart_rate) + (0.1988 * weight) + (0.2017 * age))/4.184) * 60 * totaltime_r;
        else:
            calories_burned = ((-20.4022  + (0.4472 * heart_rate) + (0.1263 * weight) + (0.074 * age))/4.184) * 60 * totaltime_r;

        avgSpd = np.average(speedList_r);
        maxSpd = np.max(speedList_r);
        pace_speed = (((distList_r[len(distList_r)-1]))/(totaltime_r));
        bestAvgSpd = np.average(speedList_b);
        bestMaxSpd = np.max(speedList_b);

        """              __init__(self, uid, rid, s_t_plots, avgSpd, maxSpd, currTime, calories_burned, bestTime, pace_speed, bestAvgSpd, bestMaxSpd, best_s_t_plot):"""
        report = rep.basic_route_report(uid, rid, speedList_r, avgSpd, maxSpd, totaltime_r, calories_burned, totaltime_b, pace_speed, bestAvgSpd, bestMaxSpd, speedList_b);
        return report;

    def doTotalReport(self, uid, rid):
        """Retrieve relevant records for the specific route, all runs of the route"""
        """uid, rid, s_t_plots, avgSpd, medSpd, maxSpd, stdDev, bestTime, bestMaxSpd, bestAvgSpd, bestMedSpd"""

        """Retrieve relevant records for the specific route, most recent run and best run"""
        speedList_r = [];
        distList_r = [0];
        distAccum_r = 0;

        """Gather user profile info"""
        age = 28;
        weight = 150;
        heart_rate = 208 - (0.7 * age);
        gender = 'male';
        calories_burned = 0;

        #myJson = json.loads("""Recent Run goes here""");
        myJson = json.load(open("sampleJson.json"));
        """ Determine Distance and speed from coordinates for recent run """
        #path to the coordinates in a standard geojson structure
        sub = myJson["features"][0]["geometry"]["coordinates"];
        totaltime_r = len(sub)*ts;
        for idx in range (0, len(sub)-1):
            distAccum_r = round(distAccum_r + (vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles), 3); #[::-1] used to reversed to allow
            distList_r.append(distAccum_r);
            speedList_r.append(round(((vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles)/ts), 3));
        """------------------------------------------------------------"""
        """------------------------------------------------------------"""
        """------------------------------------------------------------"""

        #myJson = json.loads("""Recent Run goes here""");
        myJson = json.load(open("sampleJson.json"));
        """ Determine Distance and speed from coordinates for recent run """
        #path to the coordinates in a standard geojson structure
        sub = myJson["features"][0]["geometry"]["coordinates"];
        totaltime_r = len(sub)*ts;
        for idx in range (0, len(sub)-1):
            distAccum_r = round(distAccum_r + (vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles), 3); #[::-1] used to reversed to allow
            distList_r.append(distAccum_r);
            speedList_r.append(round(((vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles)/ts), 3));


        report = rep.total_route_report();
        print("");


    def generate_report(self, report_request):
        if report_request.report_type == rep.report_type.basic_report:
            return self.doBasicReport(report_request.userid, report_request.routeid);
        elif report_request.report_type == rep.report_type.total_report:
            return self.doTotalReport(report_request.userid, report_request.routeid);
        elif report_request.report_type == rep.report_type.user_report:
            return self.doUserReport(report_request.userid, report_request.routeid);
        return None;
