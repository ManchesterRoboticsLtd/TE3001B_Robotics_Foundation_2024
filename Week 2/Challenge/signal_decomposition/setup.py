import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'signal_decomposition'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rolix57',
    maintainer_email='rolix57@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'signal_generator = signal_decomposition.signal_generator:main',
            'signal_reconstruction = signal_decomposition.signal_reconstruction:main'
        ],
    },
)
