from graph import Team, Dev, Stakeholder, Project

# simple 1 manager 3 devs 2 projects
team1 = Team("simple", "1A")
d1, d2, d3 = [team1.add_dev(d) for d in ["D1", "D2", "D3"]]
p1, p2 = [team1.add_project(p) for p in ["P1", "P2"]]
p1.add_devs([d1, d2])
p2.add_devs([d3])

# 1 manager 5 devs 5 projects
team2 = Team('simple_1_to_1', "1B")
d1, d2, d3, d4, d5 = [team2.add_dev(d)
                      for d in ["D1", "D2", "D3", "D4", "D5"]]
p1, p2, p3, p4, p5 = [team2.add_project(p)
                      for p in ["P1", "P2", "P3", "P4", "P5"]]
p1.add_devs([d1])
p2.add_devs([d2])
p3.add_devs([d3])
p4.add_devs([d4])
p5.add_devs([d5])

# 1 manager 5 devs 2 projects
team3 = Team('simple_consolidated', "1C")
d1, d2, d3, d4, d5 = [team3.add_dev(d)
                      for d in ["D1", "D2", "D3", "D4", "D5"]]
p1, p2 = [team3.add_project(p) for p in ["P1", "P2"]]
p1.add_devs([d1, d2, d3])
p2.add_devs([d4, d5])

# 1 manager 5 devs 5 projects 1 stakeholder
team4 = Team('stakeholder_1_to_1', "2A")
d1, d2, d3, d4, d5 = [team4.add_dev(d)
                      for d in ["D1", "D2", "D3", "D4", "D5"]]
p1, p2, p3, p4, p5 = [team4.add_project(p)
                      for p in ["P1", "P2", "P3", "P4", "P5"]]
s1 = team4.add_stakeholder("S1")
p1.add_devs([d1])
p2.add_devs([d2])
p3.add_devs([d3])
p4.add_devs([d4])
p5.add_devs([d5])
p1.add_stakeholders([s1])
p2.add_stakeholders([s1])
p3.add_stakeholders([s1])
p4.add_stakeholders([s1])
p5.add_stakeholders([s1])

# 1 manager 5 devs 5 projects 5 stakeholders
team5 = Team('stakeholders_4_all', "2B")
d1, d2, d3, d4, d5 = [team5.add_dev(d)
                      for d in ["D1", "D2", "D3", "D4", "D5"]]
p1, p2, p3, p4, p5 = [team5.add_project(p)
                      for p in ["P1", "P2", "P3", "P4", "P5"]]
s1, s2, s3, s4, s5 = [team5.add_stakeholder(
    s) for s in ["S1", "S2", "S3", "S4", "S5"]]
p1.add_devs([d1])
p2.add_devs([d2])
p3.add_devs([d3])
p4.add_devs([d4])
p5.add_devs([d5])
p1.add_stakeholders([s1])
p2.add_stakeholders([s2])
p3.add_stakeholders([s3])
p4.add_stakeholders([s4])
p5.add_stakeholders([s5])

# turn it to 11

# 1 manager 8 devs 4 projects 1 stakeholder
team6 = Team('big_consolidated', "3A")
d1, d2, d3, d4, d5, d6, d7, d8 = [team6.add_dev(d)
                                  for d in ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]]
p1, p2, p3, p4 = [team6.add_project(p)
                  for p in ["P1", "P2", "P3", "P4"]]
s1 = team6.add_stakeholder("S1")
p1.add_devs([d1, d5])
p2.add_devs([d2, d6])
p3.add_devs([d3, d7])
p4.add_devs([d4, d8])
p1.add_stakeholders([s1])
p2.add_stakeholders([s1])
p3.add_stakeholders([s1])
p4.add_stakeholders([s1])

# 1 manager 8 devs 8 projects 8 stakeholders
team7 = Team('hydra', "3B")
d1, d2, d3, d4, d5, d6, d7, d8 = [team7.add_dev(d)
                                  for d in ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]]
p1, p2, p3, p4, p5, p6, p7, p8 = [team7.add_project(p)
                                  for p in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]]
s1, s2, s3, s4, s5, s6, s7, s8 = [team7.add_stakeholder(
    s) for s in ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]]
p1.add_devs([d1])
p2.add_devs([d2])
p3.add_devs([d3])
p4.add_devs([d4])
p5.add_devs([d5])
p6.add_devs([d6])
p7.add_devs([d7])
p8.add_devs([d8])
p1.add_stakeholders([s1])
p2.add_stakeholders([s2])
p3.add_stakeholders([s3])
p4.add_stakeholders([s4])
p5.add_stakeholders([s5])
p6.add_stakeholders([s6])
p7.add_stakeholders([s7])
p8.add_stakeholders([s8])
