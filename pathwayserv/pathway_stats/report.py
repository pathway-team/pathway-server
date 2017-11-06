import json;

class report:
    def __init__(self, uid, rid, s_t_plots, pace_speed, avgSpd, medSpd, maxSpd, currTime, calories_burned):
        self.userid = uid;
        self.routeid = rid;
        self.s_t_plotsx = s_t_plots;
        self.pace_speed = pace_speed;
        self.avgSpeed = avgSpd;
        self.medSpeed = medSpd;
        self.maxSpeed = maxSpd;

    def audit(self):
        return true;

    def sendToDatabase(self):
        return "";

    def sendToUser(self):
        return json.dumps(self.__dict__);

class basic_route_report(report):
    def __init__(self, uid, rid, s_t_plots, pace_speed, avgSpd, medSpd, maxSpd, currTime, calories_burned, bestTime, bestAvgSpd, bestMedSpd, bestMaxSpd, best_s_t_plot):
        super().__init__(uid, rid, s_t_plots, pace_speed, avgSpd, medSpd, maxSpd, currTime, calories_burned);
        self.bestTime = bestTime;
        self.bestMaxSpd = bestMaxSpd;
        self.bestAvgSpd = bestAvgSpd;
        self.bestMedSpd = bestMedSpd;
        self.best_s_t_plot = best_s_t_plot;
        
    def audit(self):
        return true;

    def sendToDatabase(self):
        return "";

    def sendToUser(self):
        return "Basic|" + super().sendToUser();

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

class full_user_report(report):
    def __init__(self, uid, rid, s_t_plots, pace_plot, avgSpd, medSpd, maxSpd, total_dist, avg_dist_route, performance_plotx, performance_ploty, total_time):
        super().__init__(uid, rid, s_t_plots, pace_plot, avgSpd, medSpd, maxSpd);
        self.total_dist = total_dist;
        self.avg_dist_route = avg_dist_route;
        self.performance_plotx = performance_plotx;
        self.performance_ploty = performance_ploty;
        self.total_time = total_time;

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
    full_report = 2;
