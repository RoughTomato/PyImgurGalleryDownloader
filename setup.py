from setuptools import setup

setup(name='pyImgurDownloader',
      version='0.1',
      description='Small script in Python that downloads gallery contents from Imgur links.',
      url='https://github.com/RoughTomato/PyImgurGalleryDownloader',
      author='Amadeusz Dabkowski',
      author_email='adabkowski93@gmail.com',
      license='GPLv3',
      packages=['pyImgurDwn'],
      install_requires=[
        'argparse',
        'pytest'
      ],
      zip_safe=False
)
