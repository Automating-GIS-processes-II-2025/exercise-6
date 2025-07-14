from points_decorator import points
import xarray
import inspect
import os
import pandas as pd
import geopandas as gpd
import pyproj
import pytest

class TestProblem2:

    @points(0.5, "Problem 2, Part 1: Did you import the raster data?")
    def test_problem_2_part_1(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"
        variables = section_data[section]['variables']

        assert isinstance(variables['sentinel_raster'], xarray.core.dataarray.DataArray)

    @points(0.25, "Problem 2, Part 1: Did you check the CRS of the data?")
    def test_problem_2_part_1_crs(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"
        variables = section_data[section]['variables']

        assert variables['data_crs'] == 'EPSG:32635'
        
    @points(0.25, "Problem 2, Part 1: Did you check the resolution of the data?")
    def test_problem_2_part_1_resolution(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"
        variables = section_data[section]['variables']

        assert variables['spatial_resolution'] == 10

    @points(1, "Problem 2, Part 2: Did check the total number of pixels?")
    def test_problem_2_part_2(self, problem2):
        section_data, namespace = problem2
        section = "Part 2"
        variables = section_data[section]['variables']

        assert variables['total_pixels'] == 7895160

    @points(1, "Problem 2, Part 2: Did you use subplots to plot the NIR and Red bands?")
    def test_problem_2_part_2_plot(self, problem2):
        section_data, namespace = problem2
        section = "Part 2"
        source = section_data[section]['source']

        assert "subplots" in source


    @points(3, "Problem 2, Part 3: Did you calculate the NDVI?")
    def test_problem_2_part_3_ndvi(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        variables = section_data[section]['variables']

        #assert isinstance(variables['NDVI'], xarray.core.dataarray.DataArray)
        assert variables['NDVI'].values.mean() == pytest.approx(0.74, abs=0.01)

    @points(1, "Problem 2, Part 3: Did you plot the NDVI?")
    def test_problem_2_part_3_plot(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        variables = section_data[section]['variables']

        assert variables['NDVI'].plot() is not None

    @points(1, "Problem 2, Part 3: Did you save the NDVI as a GeoTIFF?")
    def test_problem_2_part_3_save(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        variables = section_data[section]['variables']

        assert os.path.exists('NDVI_output.tif')
        

    @points(4, "Problem 2, Part 4: Did you reclassify the NDVI values?")
    def test_problem_2_part_4_reclass(self, problem2):
        section_data, namespace = problem2
        section = "Part 4"
        variables = section_data[section]['variables']
 
        assert variables['reclassified_ndvi'].mean() == pytest.approx(2.88, abs=0.01)
    