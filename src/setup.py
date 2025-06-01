from setuptools import setup
import os 
from glob import glob 

package_name = 'my_autonomous_car'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'), glob('launch/*')  )  ,
        (os.path.join('share',package_name,'config'), glob('config/*') ),
        (os.path.join('share',package_name,'world/parking'), glob('world/parking/*') ),

              ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sathwik',
    maintainer_email='sathwik@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'map_publisher_node = my_autonomous_car.map_publisher:main',
            'sdf_spawner = my_autonomous_car.entity_spawner:main',
            'parking_solver = my_autonomous_car.parking_solver:main'
        ],
    },
)
