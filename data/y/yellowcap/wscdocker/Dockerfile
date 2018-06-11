FROM ubuntu:14.04  
# Connect to ubuntugis  
RUN echo "deb http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu
trusty main " >> /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu
trusty main" >> /etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 314DF160  
  
# Update apt packages  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install Utilities  
RUN apt-get install -y curl git vim build-essential python-setuptools python-
dev python-pip python-software-properties  
  
# DB & GIS  
RUN apt-get install -y postgresql-server-dev-9.3 postgis gdal-bin  
  
# Apache and mod-wsgi  
RUN apt-get install -y apache2 libapache2-mod-wsgi  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
# Sass  
RUN apt-get install -y ruby  
RUN gem install sass  
  
# r.js, lessc  
RUN apt-get -y install npm  
RUN npm install -g requirejs less  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Autoprefixer (css goodness for browser support)  
RUN npm install -g less-plugin-autoprefix  
  
# Bower  
RUN npm install -g bower  
  
# Java, Selenium Server, Firefox, Virtual FrameBuffer and fonts  
RUN apt-get install -y default-jre  
RUN apt-get install -y firefox  
RUN apt-get install -y xvfb  
RUN apt-get install -y xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-
cyrillic  
RUN mkdir /java-apps  
RUN curl -o /java-apps/selenium-server-standalone-2.45.0.jar http://selenium-
release.storage.googleapis.com/2.45/selenium-server-standalone-2.45.0.jar  
ENV DISPLAY :99  
# Supervisor  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# Image libraries  
RUN apt-get install -y libjpeg8 libjpeg8-dev  
RUN apt-get build-dep -y python-imaging  
  
# Python dependencies  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  

