# pip install neo4j-driver if not using py2neo

from py2neo import Graph, Node, Relationship

# clear Graph every time
graph = Graph(bolt="bolt://localhost:7687",
              user="neo4j", password="graph")
graph.delete_all()


class Team:
    def __init__(self, name, manager=""):
        self.name = name
        self.manager = manager
        self.manager_node = None

        self.dev_list = []
        self.project_list = []

        self.graph = Graph(bolt="bolt://localhost:7687",
                           user="neo4j", password="graph")

        self.create_manager()

    def start_tx(self):
        return self.graph.begin()

    def add_dev(self, name):
        tx = self.start_tx()
        d = Dev(name=name, team=self)
        dn = self.create_node(node_type="Dev", name=name)
        d.set_node(dn)

        tx.create(dn)
        tx.commit()

        # create the mgr relationship
        self.create_relationship(self.manager_node, "manages", dn)
        return d

    def add_stakeholder(self, name):
        tx = self.start_tx()
        s = Stakeholder(name=name, team=self)
        sn = self.create_node(node_type="Stakeholder", name=name)
        s.set_node(sn)

        tx.create(sn)
        tx.commit()

        return s

    def add_project(self, name):
        tx = self.start_tx()
        p = Project(name=name, team=self)
        pn = self.create_node(node_type="Project", name=name)
        p.set_node(pn)

        tx.create(pn)

        tx.commit()

        return p

    def create_relationship(self, n1, edge_type, n2):
        tx = self.start_tx()
        ab = Relationship(n1, edge_type, n2)
        tx.create(ab)
        tx.commit()

    def create_node(self, node_type="Person", name=""):
        return Node(node_type, name=name)

    def create_manager(self):
        tx = self.start_tx()
        mgr = Node("Manager", name=self.manager)
        tx.create(mgr)
        self.manager_node = mgr
        tx.commit()


class Dev:
    # TODO: add default prefix and rel type & abstract to Person class
    def __init__(self, name="", team=None):
        self.name = name
        self.team = team
        self.node = None

        self.projects_list = []

    def set_node(self, node):
        self.node = node

    def add_project(self, project):
        # should only be called by project
        self.projects_list.append(project)


class Stakeholder:
    def __init__(self, name="", team=None):
        self.name = name
        self.team = team
        self.node = None

        self.projects_list = []

    def set_node(self, node):
        self.node = node

    def add_project(self, project):
        self.projects_list.append(project)


class Project:
    def __init__(self, name="", team=None):
        self.name = name
        self.team = team
        self.node = None

        self.devs_list = []
        self.stakeholder_list = []

    def set_node(self, node):
        self.node = node

    def add_devs(self, devs=None):
        for d in devs:
            self.devs_list.append(d)
            d.add_project(self)

            self.team.create_relationship(d.node, "works_on", self.node)

    def add_stakeholders(self, ppl=None):
        for p in ppl:
            self.stakeholder_list.append(p)
            p.add_project(self)

            self.team.create_relationship(p.node, "owns", self.node)
