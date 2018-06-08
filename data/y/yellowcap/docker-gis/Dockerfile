FROM ubuntu:14.04  
# Connect to ubuntugis  
RUN echo "deb http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu
trusty main " >> /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu
trusty main" >> /etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 314DF160  
  
# update apt cache and upgrade  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install Utilities  
RUN apt-get install -y curl git vim build-essential python-setuptools python-
dev python-pip python-software-properties  
  
# DB & GIS  
RUN apt-get install -y postgresql-server-dev-9.3 postgis mapserver-bin python-
mapscript python-gdal  
  
# Apache and mod-wsgi  
RUN apt-get install -y apache2 libapache2-mod-wsgi  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
# Sass  
RUN apt-get install -y ruby  
RUN gem install sass  
  
# Less and r.js  
RUN apt-get -y install npm  
RUN npm install -g requirejs less  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Bower  
RUN npm install -g bower  
  
# aws cli  
RUN apt-get -y install awscli  
  
# Java, Selenium Server, Firefox, Virtual FrameBuffer and fonts  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y default-jre  
RUN apt-get install -y firefox  
RUN apt-get install -y xvfb  
RUN apt-get install -y xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-
cyrillic  
RUN mkdir /java-apps  
RUN curl -o /java-apps/selenium-server-standalone-2.43.1.jar http://selenium-
release.storage.googleapis.com/2.43/selenium-server-standalone-2.43.1.jar  
ENV DISPLAY :99  
# Supervisor  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# NumPy & SciPy  
RUN apt-get install -y python-numpy python-scipy  
  
# Mezzanine related image libraries  
RUN apt-get install -y libjpeg8 libjpeg8-dev  
RUN apt-get build-dep -y python-imaging  

