import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ponderada'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vzeferino',
    maintainer_email='vitor.queiroz@sou.inteli.edu.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "go_to_pose = ponderada.go_to_pose:main",
            "set_initial_pose = ponderada.initial_pose:main"
            "nav = ponderada.nav:main"
        ],
    },
)