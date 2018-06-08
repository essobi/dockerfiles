FROM ubuntu:latest  
MAINTAINER bencevans  
  
RUN apt-get -q update  
  
# Install packages for python and sound  
RUN apt-get -y install wget \  
alsa-base \  
alsa-utils \  
alsa-oss \  
flac \  
python-setuptools \  
python-pip  
  
# Install Mopidy  
RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add -  
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list
http://apt.mopidy.com/mopidy.list  
RUN apt-get -q update  
RUN apt-get -y install mopidy mopidy-soundcloud mopidy-spotify  
RUN easy_install cherrypy>=3.2.2  
  
# Shared volume  
RUN mkdir /var/media  
VOLUME ["/var/media"]  
  
# Add configuration  
RUN mkdir -p /root/.config/mopidy  
ADD mopidy.conf /root/.config/mopidy/mopidy.conf  
  
# Install plugins  
RUN pip install Mopidy-API-Explorer  
RUN pip install Mopidy-Youtube  
RUN pip install Mopidy-Moped  
# Add this if you want spotify  
RUN pip install Mopidy-Mopify  
  
CMD ["mopidy"]  

