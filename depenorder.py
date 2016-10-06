"""
depenorder.py


TODO
"""

import random


class DepenNode(object):
    """
    dependency node object contains all need data to mantane a depenendcies tree
    """
    def __init__(self, proj_id, depenendcies=None, status=None):  # TODO set all
        self.statuses = ('INIT', 'WORKING', 'PROCESSED')
        if depenendcies is None:
            depenendcies = []
        if status is None:
            status = 'INIT'
        self.proj_id = proj_id
        self.depenendcies = depenendcies
        self.status = status

    def __repr__(self):
        return '{} : {} : {}'.format(self.proj_id, self.status, str(self.depenendcies))

    def add_depenendcie(self, depenend_proj_id):
        temp = self.depenendcies
        temp.append(depenend_proj_id)
        self.depenendcies = temp

    def set_status(self, status):
        if status in self.statuses:
            self.status = status


class DepenendcieTree(object):
    """
    Depenendcie Tree a dictionary made of dependency nodes
    Tree dictionary keyed on proj_id value is dependency node object
    """
    def __init__(self):
        self._proj_table = {}
        #super(DepenendcieTree, self).__init__()

    def add_proj_list(self, proj_list):
        """ Adds proj_list, mechanism of building a tree"""
        for proj in proj_list:
            new_proj_node = DepenNode(proj)
            self._proj_table[proj] = new_proj_node

    def add_depenendcie_list(self, depenendcie_list):
        for depen in depenendcie_list:
        #for depen in depenendcie_list:
            temp_proj_node = self._proj_table[depen[1]]
            temp_proj_node.add_depenendcie(depen[0])
            self._proj_table[depen[1]] = temp_proj_node

    def set_proj_status(self, proj, status):
            if proj in self._proj_table:
                temp_proj_node = self._proj_table[proj]
                temp_proj_node.set_status(status)
                self._proj_table[proj] = temp_proj_node

    def list(self):
        str_out = ''
        for proj, proj_node in self._proj_table.items():
            str_out += '{} : {} : {}\n'.format(proj, proj_node.status,
                str(proj_node.depenendcies))
        return str_out



class DepenOrder(DepenendcieTree):
    """
    Main object contains all need data to calc dependency order
    """
    def __init__(self, proj_list, depenendcie_list):
        super(DepenOrder, self).__init__()
        self.proj_targets = proj_list[:]
        self.depenendcie_list = depenendcie_list  # target
        self.add_proj_list(proj_list)
        self.add_depenendcie_list(depenendcie_list)

        #self.depen_order = []

    def get_new_rand_proj(self):
        i = random.randint(0, len(self.proj_targets) - 1)
        emit = self.proj_targets[i]
        self.proj_targets.remove(emit)
        return emit

    def invert_list(self, a_list):
        lenth = len(a_list)
        new_list = [' '] * lenth
        for i in range(lenth -1 , -1, -1):           
            new_list[lenth - i -1] = a_list[i]
        return new_list

    def sub_depen_list(self, start_proj, depen_order):
     
        proj = start_proj
        prj_depen_list = self._proj_table[proj].depenendcies
        # visit all proj(s) who are depen on start_proj
        while prj_depen_list:            
            proj = prj_depen_list.pop()
            # TODO graph not looping, cheek proj not 'WORKING'
            if self._proj_table[proj].status == 'WORKING':
                #error graph loop found at proj
                return proj
            if (self._proj_table[proj].status != 'PROCESSED'):
                self._proj_table[proj].set_status('WORKING')
                depen_order = self.sub_depen_list(proj, depen_order)
                depen_order = [proj] + depen_order
                #print 'Biuld ->  proj', proj, 'depen_order', depen_order, 'prj_depen_list', prj_depen_list
                self._proj_table[proj].set_status('PROCESSED')
                if (proj in self.proj_targets):
                    self.proj_targets.remove(proj)
        return depen_order

    def calc_order(self):
        depen_order = []
        x = 0
        while self.proj_targets:
            new_rand_proj = self.get_new_rand_proj()
            #print '\nBEFOR: new_rand_proj', "'" + new_rand_proj + "'", 'self.proj_targets', self.proj_targets   
            depen_order = [new_rand_proj] + self.sub_depen_list(new_rand_proj, depen_order)
            self._proj_table[new_rand_proj].set_status('PROCESSED')
            #print 'AFTER: depen_order', depen_order     
        return depen_order

    def build_order_validation(self):
        #validate build order, a correctness test
        pass

######################
# nd = DepenNode('a')
# print(nd)
# nd.add_depenendcie('b')
# nd.add_depenendcie('s')

# print(nd)
# print(nd.status)

# test add_proj_list

proj_list = ['a', 'b', 'c', 'd', 'e', 'f']
depenendcie_list = [['d', 'a'], ['b', 'f'], ['d', 'b'], ['a', 'f'], ['c', 'd']]

# dep_tree = DepenendcieTree()
# dep_tree.add_proj_list(proj_list)
# print dep_tree.list()
# dep_tree.add_depenendcie_list(depens_list)
# print dep_tree.list()

td = DepenOrder(proj_list, depenendcie_list)
print td.list()
#print td.get_new_rand_proj()
#print td.invert_list(['1','2','3','4'])
start_at = 'b'

#print td.sub_depen_list(start_at, depen_order)
print 'td.calc_order()',td.calc_order()