"""
Unit test fixture for depenorder.py


TODO
"""

import unittest
from depenorder import *


#  Basic creation and detection
class TestDepenorder(unittest.TestCase):

    def setUp(self):
        self.projects = ['a', 'b', 'c', 'd', 'e', 'f']
        self.dependencies = [['d', 'a'], ['b', 'f'], ['d', 'b'], ['a', 'f'], ['c', 'd']]
        self.expected_order = ['f', 'e', 'a', 'b', 'd', 'c']
    def tearDown(self):
        pass

    def test_01_dtree_add_proj_list(self):
        #setup
        dep_tree = DepenendcieTree()
        dep_tree.add_proj_list(self.projects)
        actual = dep_tree.list()
        expected = '''a : INIT : []\nc : INIT : []\nb : INIT : []\ne : INIT : []\nd : INIT : []\nf : INIT : []\n'''
        self.assertEqual(actual, expected)

    def test_dtree_01_add_depenendcie_list(self):
        #setup
        dep_tree = DepenendcieTree()
        dep_tree.add_proj_list(self.projects)
        dep_tree.add_depenendcie_list(self.dependencies)
        actual = dep_tree.list()
        expected = '''a : INIT : ['d']\nc : INIT : []\nb : INIT : ['d']\ne : INIT : []\nd : INIT : ['c']\nf : INIT : ['b', 'a']\n'''
        self.assertEqual(actual, expected)

    def test_dtree_02_set_proj_status(self):
        # setup
        dep_tree = DepenendcieTree()
        dep_tree.add_proj_list(self.projects)
        dep_tree.add_depenendcie_list(self.dependencies)
        # test
        proj = 'a'
        status = 'WORKING'
        dep_tree.set_proj_status(proj, status)
        actual = dep_tree.list()
        expected = '''a : WORKING : ['d']\nc : INIT : []\nb : INIT : ['d']\ne : INIT : []\nd : INIT : ['c']\nf : INIT : ['b', 'a']\n'''
        self.assertEqual(actual, expected)

    def test_dorder_01_init_list(self):
        # setup
        td = DepenOrder(self.projects, self.dependencies)
        # test
        actual = td.list()
        expected = '''a : INIT : ['d']\nc : INIT : []\nb : INIT : ['d']\ne : INIT : []\nd : INIT : ['c']\nf : INIT : ['b', 'a']\n'''
        self.assertEqual(actual, expected)

    def test_dorder_02_get_new_rand_proj(self):
        # setup
        td = DepenOrder(self.projects, self.dependencies)
        # test
        raw_actual = td.get_new_rand_proj()
        actual = (raw_actual in self.projects)
        expected = True
        self.assertEqual(actual, expected)

    def test_dorder_03_invert_list(self):
        td = DepenOrder([], [])
        actual = td.invert_list(['1','2','3','4'])
        expected = ['4', '3', '2', '1']
        self.assertEqual(actual, expected)
    def test_dorder_04_sub_depen_list(self):
        # setup
        td = DepenOrder(self.projects, self.dependencies)
        proj = 'f'
        depen_order = []
        # test
        actual = [proj] + td.sub_depen_list(proj, depen_order)
        expected = ['f', 'b', 'a', 'd', 'c']
        self.assertEqual(actual, expected)

    def test_dorder_05_calc_order(self):
        # setup
        td = DepenOrder(self.projects, self.dependencies)
        actual = td.build_order_validation()
        expected = True
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
