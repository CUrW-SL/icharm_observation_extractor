from setuptools import setup

setup(
    name='icharm_observation_extractor',
    version='1.0.0',
    install_requires=['pandas', 'numpy', 'curwmysqladapter'],
    dependency_links=["git+https://github.com/CUrW-SL/CurwMySQLAdapter.git"],
    url='https://github.com/CUrW-SL/icharm_observation_extractor',
    license='MIT',
    author='thilinamad',
    author_email='madumalt@gmail.com',
    description='Observation data extractor from Icharm.'
)
