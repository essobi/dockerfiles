##  
# mapic/geo:latest  
#  
FROM mapic/xenial:latest  
  
# maintainer  
MAINTAINER knutole@mapic.io  
  
# install java  
RUN echo "Installing Java"  
RUN add-apt-repository ppa:openjdk-r/ppa > /dev/null  
RUN apt-get update -y > /dev/null  
RUN apt-get install -y openjdk-8-jdk > /dev/null  
  
# install mysql  
RUN echo "Installing MySQL"  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server mysql-
client > /dev/null  
  
# install graphics magick  
RUN echo "Installing Graphics Magick"  
ADD ./install-graphicsmagick.sh /tmp/install-graphicsmagick.sh  
RUN sh /tmp/install-graphicsmagick.sh > /dev/null  
  
# install phantom-js  
RUN echo "Installing PhantomJS"  
ADD ./install-phantomjs.sh /tmp/install-phantomjs.sh  
RUN sh /tmp/install-phantomjs.sh > /dev/null  
  
# install gdal  
RUN echo "Installing Gdal"  
ADD ./install-gdal.sh /tmp/install-gdal.sh  
RUN bash /tmp/install-gdal.sh > /dev/null  
  
# install boost  
RUN echo "Installing Boost"  
ADD ./install-boost.sh /tmp/  
RUN bash /tmp/install-boost.sh > /dev/null  
  
# install harfbuzz  
RUN echo "Installing Harfbuzz"  
ADD ./install-harfbuzz.sh /tmp/  
RUN bash /tmp/install-harfbuzz.sh > /dev/null  
  
# # install mapnik  
# RUN echo "Installing Mapnik"  
# ADD ./install-mapnik.sh /tmp/  
# RUN bash /tmp/install-mapnik.sh > /dev/null  
# # install yarn  
RUN echo "Installing Yarn"  
# ADD ./install-yarn.sh /tmp/  
# RUN bash /tmp/install-yarn.sh > /dev/null  
RUN rm /etc/apt/sources.list.d/*  
RUN apt-get clean > /dev/null  
  
# install postgis  
RUN echo "Installing PostGIS"  
RUN sudo add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable > /dev/null  
RUN apt-get update -y > /dev/null  
RUN apt-get install -y postgresql-client postgis libpq-dev python-psycopg2
postgresql > /dev/null  
  
# # workdir  
# WORKDIR /data  
# # volume  
# VOLUME ["/data"]

