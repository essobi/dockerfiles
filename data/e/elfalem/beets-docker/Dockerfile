#  
# Development image (testing tools included)  
#  
FROM elfalem/beets-docker:base  
MAINTAINER elfalem <elfalem@gmail.com>  
  
#dev tools  
RUN pip install tox sphinx nose  
  
#dev dependencies  
RUN pip install beautifulsoup4 flask mock pylast rarfile responses pyxdg
pathlib python-mpd2 discogs-client  
  
WORKDIR /code  
  
USER beets  
  
  

