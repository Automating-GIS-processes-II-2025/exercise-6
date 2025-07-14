from points_decorator import points
import inspect
import os
import pandas as pd
import geopandas as gpd
import pyproj
import xarray

class TestProblem1:

    @points(1, "Problem 1, Part 1: Did you import the raster data?")
    def test_problem_1_part_1(self, problem1):
        section_data, namespace = problem1
        section = "Part 1"
        variables = section_data[section]['variables']

        assert isinstance(variables['temp_raster'], xarray.core.dataarray.DataArray)


    @points(1, "Problem 1, Part 2: Did you iterate through the raster bands?")
    def test_problem_1_part_2_loop(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"
        source = section_data[section]['source']

        assert any(keyword in source for keyword in ["for", "while"])

    @points(1, "Problem 1, Part 2: Variable ´day_number´ is not correct!")
    def test_problem_1_part_2_day(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"
        variables = section_data[section]['variables']

        assert variables['day_number'] == 219


    @points(1, "Problem 1, Part 3: Did you select the band with the hottest temperature and assign it to the variable ´hot_day_raster´?")
    def test_problem_1_part_3_hotdayraster(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"
        variables = section_data[section]['variables']

        assert len(variables['hot_day_raster']) == 116

    @points(1, "Problem 1, Part 3: Did you calculate the mean temperature and assign it to the variable ´average_temp´?")
    def test_problem_1_part_3_average_temp(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"
        variables = section_data[section]['variables']

        assert round((variables['average_temp']),2) == 21.01

    
    @points(2, "Problem 1, Part 3: Did you calculate the min and max temperature, assign them to the variables ´min_temp´ and ´max_temp´ and round to two decimals?")
    def test_problem_1_part_3_minmax_temp(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"
        variables = section_data[section]['variables']

        assert variables['min_temp'] == 11.3
        assert variables['max_temp'] == 26.9

    @points(1, "Problem 1, Part 4: Did you convert the temperature units and plot the data?")
    def test_problem_1_part_4(self, problem1):
        section_data, namespace = problem1
        section = "Part 4"
        variables = section_data[section]['variables']
        source = section_data[section]['source']

        assert round(variables['hot_day_fahr'].min().item(),2) == 52.34

        assert 'plot' in source
        