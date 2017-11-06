from . import report as rep;
import json;
import numpy as np;
import statistics as stats;
from geopy.distance import vincenty;

class ReportFactory:


    def doFullReport(self, uid, rid):
        """ Retrieve relevant records for all routes from user's"""
        print("");

    def doBasicReport(self, uid, rid):
        """Retrieve relevant record for the specific route: most recent run and best run"""
        speedList_r = [];
        distList_r = [0];
        distAccum_r = 0;
        ts = 5;

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
        sub = myJson["features"][0]["geometry"]["coordinates"];
        totaltime_r = len(sub)*ts;
        for idx in range (0, len(sub)-1):
            distAccum_r = round(distAccum_r + (vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles), 3); #[::-1] used to reversed to allow
            distList_r.append(distAccum_r);
            speedList_r.append(round(((vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles)/ts), 3));
        
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
        sub = myJson["features"][0]["geometry"]["coordinates"];
        totaltime_b = len(sub)*ts;
        for idx in range (0, len(sub)-1):
            distAccum_b = round(distAccum_b + (vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles), 3);
            distList_b.append(distAccum_b);
            speedList_b.append(round(((vincenty(tuple(sub[idx])[::-1], tuple(sub[idx+1])[::-1]).miles)/ts), 3));

        if gender == "male":
            calories_burned = ((-55.0969 + (0.6309 * heart_rate) + (0.1988 * weight) + (0.2017 * age))/4.184) * 60 * totaltime_r;
        else:
            calories_burned = ((-20.4022  + (0.4472 * heart_rate) + (0.1263 * weight) + (0.074 * age))/4.184) * 60 * totaltime_r;
        """              __init__(self, uid, rid, s_t_plots, pace_speed, avgSpd, medSpd, maxSpd, currTime, bestTime, bestMaxSpd, bestAvgSpd, bestMedSpd, best_s_t_plot):"""
        report = rep.basic_route_report(uid, rid, speedList_r, (((distList_r[len(distList_r)-1]))/(totaltime_r)), np.average(speedList_r), np.median(speedList_r), np.max(speedList_r), totaltime_r, calories_burned, totaltime_b, np.average(speedList_b), np.median(speedList_b), np.max(speedList_b), speedList_b);
        return report;

    def doTotalReport(self, uid, rid):
        """Retrieve relevant records for the specific route, all runs of the route"""
        """uid, rid, s_t_plots, avgSpd, medSpd, maxSpd, stdDev, bestTime, bestMaxSpd, bestAvgSpd, bestMedSpd"""

        """Retrieve relevant records for the specific route, most recent run and best run"""
        speedList_r = [];
        distList_r = [0];
        distAccum_r = 0;
        ts = 5;

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
        elif report_request.report_type == rep.report_type.full_report:
            return self.doFullReport(report_request.userid, report_request.routeid);
        return None;
