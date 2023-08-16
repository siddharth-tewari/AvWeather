from distutils.core import setup
import setuptools

setup(
  name = 'AvWeather',         # How you named your package folder (MyLib)
  packages = ['AvWeather'],   # Chose the same as "name"
  version = '2.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Aviation METAR and TAF Reports',   # Give a short description about your library
  author = 'Siddharth Tewari',                   # Type in your name
  url = 'https://github.com/siddharth-tewari/AvWeather',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/siddharth-tewari/AvWeather/archive/refs/tags/02.tar.gz',    # I explain this later on
  keywords = ['Aviation', 'Aviation Weather', 'Metar', 'TAF'],   # Keywords that define your package best
  classifiers=[
    'Flight',     
    'Aviation',
    'Aircraft',
    'METAR',
    'TAF',
  ],
)
