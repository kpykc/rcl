import os
from setuptools import setup, find_packages

version = "1.0"

description = """Code for retina camera localization"""  # TODO

long_description = description    # TODO

setup(name='RCL',
      url='',
      description=description,
      long_description=long_description,
      package_data={'':['*.*']},
      keywords="",
      license="",

      classifiers=[
        'Development Status :: 4 - Beta',
      ],

      version=version,

      download_url=
        'http://github.com/AndreaCensi/rcl/tarball/%s' % version,

      package_dir={'':'src'},
      packages=find_packages('src'),
      install_requires=[
        'ConfTools>=1.0,<2',
        'PyVehicles',
        'PyContracts>=1.2,<2',
        'PyYAML',
        'python-cjson',
        'PyGeometry'
      ],
      tests_require=['nose>=1.1.2,<2'],
      entry_points={
         'console_scripts': [
                'aer_read_log = rcl.library.aerlog.load_aer_logs:main',
                'aer_simple_stats = rcl.programs.aer_simple_stats:main',
                'rcl_detect = rcl.programs.detect:rcl_detect_main',
                'rcl_demo_vehicles = rcl.programs.rcl_demo_vehicles:main',
                'rcl_demo_plots = rcl.programs.rcl_demo_plots:main',
                'rcl_frequency = rcl.programs.rcl_frequency:main',
                'rcl_frequency_one = rcl.programs.rcl_frequency_one:main',
                'rcl_many_stats = rcl.programs.rcl_many_stats:main',
                'rcl_filter = rcl.programs.rcl_filter:main',
                'rcl_filter_phase = rcl.programs.rcl_filter_phase:main'
                
           # 'vehicles_print_config = '
           #      'vehicles.programs.print_config:main',
           # 'vehicles_display_demo_simulations = '
           #      'vehicles.programs.display_demos.simulations:main',
           # 'vehicles_display_demo_skins = '
           #      'vehicles.programs.display_demos.skins:main',
           # 'vehicles_display_demo_vehicles = '
           #      'vehicles.programs.display_demos.vehicles:main',
           # 'vehicles_inspect_textures = '
           #      'vehicles.programs.inspect_textures:main',
           #  'vehicles_create_olympics_configs = '
           #      'vehicles_boot.create_olympics_configs:main',
           # 'vehicles_fps = '
           #      'vehicles.unittests.fps_test:main',
        ]
      }
)

