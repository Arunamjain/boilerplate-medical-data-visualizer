import medical_data_visualizer
import unittest
import test_module

unittest.main(module='test_module', exit=False, verbosity=2)

medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()
