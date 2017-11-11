import json;

class report:
    def __init__(self, uid, rid, s_t_plots, avgSpd, maxSpd, currTime, calories_burned):
        self.userid = uid;
        self.routeid = rid;
        self.s_t_plotsx = s_t_plots;
        self.avgSpeed = avgSpd;
        self.maxSpeed = maxSpd;

    def audit(self):
        return true;

    def sendToDatabase(self):
        return "";

    def sendToUser(self):
        return json.dumps(self.__dict__);
"""
Basic Route Report

"""
class basic_route_report(report):
    def __init__(self, uid, rid, s_t_plots, avgSpd, maxSpd, currTime, calories_burned, bestTime, pace_speed, bestAvgSpd, bestMaxSpd, best_s_t_plot):
        super().__init__(uid, rid, s_t_plots, avgSpd, maxSpd, currTime, calories_burned);
        self.bestTime = bestTime;
        self.pace_speed = pace_speed;
        self.bestMaxSpd = bestMaxSpd;
        self.bestAvgSpd = bestAvgSpd;
        self.best_s_t_plot = best_s_t_plot;

    def audit(self):
        return true;

    def sendToDatabase(self):
        return "";

    def sendToUser(self):
        return "Basic|" + super().sendToUser();
"""

"""
class total_route_report(basic_route_report):
    def __init__(self, uid, rid, s_t_plots, pace_speed, avgSpd, medSpd, maxSpd, currTime, calories_burned, bestTime, bestAvgSpd, bestMedSpd, bestMaxSpd, best_s_t_plot, rec_s_t_plots):
        super().__init__(self, uid, rid, s_t_plots, pace_speed, avgSpd, medSpd, maxSpd, currTime, calories_burned, bestTime, bestAvgSpd, bestMedSpd, bestMaxSpd, best_s_t_plot, rec_s_t_plots);
        self.rec_s_t_plots = rec_s_t_plots;


    def audit(self):
        return true;

    def sendToDatabase(self):
        return "";

    def sendToUser(self):
        return "Total|" + super().sendToUser();

"""
User Report
Contains data about user's statistics for all their runs of routes. This data
will be used for the user profile subsystem and the achievements of the social
subsystem.
Variables:
    uid             : user id
    rid             : route id
    s_t_plot        : speed/time plot for a user over their history of runs
    avgSpd          : Average speed over all routes run by this user
    maxSpd          : Max speed for this user
    total_dist      : total distance for the user across run all routes
    avg_dist_route  : average distance a user runs
    total_time      : total time the application has been used
    total_calories  : estimate of total calories burned for this user
    history_histo   : history histogram for number of attempts made by user
"""
class user_report(report):
    def __init__(self, uid, rid, s_t_plots, pace_plot, avgSpd, maxSpd, total_dist, avg_dist_route, total_time, total_calories, history_histo):
        super().__init__(uid, rid, s_t_plots, pace_plot, avgSpd, maxSpd);
        self.total_dist = total_dist;
        self.avg_dist_route = avg_dist_route;
        self.total_time = total_time;
        self.total_num_routes = total_num_routes;
        self.total_num_runs = total_num_runs;
        self.activity_hist = activity_hist;
        self.total_calories = total_calories;
        self.history_histo = history_histo;

    def audit(self):
        return true;

    def sendToDatabase(self):
        return "";

    def sendToUser(self):
        return "User|" + super().sendToUser();

class report_request:
    def __init__(self, rep_type, user_id, route_id):
        self.report_type = rep_type;
        self.userid = user_id;
        self.routeid = route_id;

class report_type:
    basic_report = 0;
    total_report = 1;
    user_report = 2;
