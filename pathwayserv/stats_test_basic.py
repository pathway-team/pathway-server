import pathway_stats.report as rep;
import pathway_stats.report_factory as report_factory;

request = rep.report_request(rep.report_type.basic_report, 0, 0);
factory = report_factory.ReportFactory();
r = factory.generate_report(request);

print(r.sendToUser());
f = open("reporttest.txt", "w");
f.write(r.sendToUser());
f.close();
print("Done!");
