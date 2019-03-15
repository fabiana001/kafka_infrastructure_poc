from setuptools import setup, find_packages

setup(name='ARGOInfrastructure',
      version='0.0.1',
      description='Kafka stream from myslq to elasticsearch',
      author='prometeia',
      author_email='fabiana.lanotte@prometeia.com',
      packages=find_packages(where='src'),
      package_dir={'':'src'},
      setup_requires=[],
      install_requires=[
          'pytest'
      ],
      package_data={
          # If any package contains *.txt include them:
          '': ['avro/*.avsc']}
)
