FROM python:2.7  
MAINTAINER Person Sebastien <personseb@yahoo.fr>  
  
# no need for confirmation  
ENV DEBIAN_FRONTEND noninteractive  
  
# Recommends are as of now still abused in many packages  
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/no-recommends  
RUN echo "APT::Get::Assume-Yes "true";" > /etc/apt/apt.conf.d/always-yes  
  
# see http://www.garron.me/en/blog/ubuntu-deb-proxy-cache.html  
#RUN echo 'Acquire::http { Proxy "http://192.168.0.32:3142"; };' >
/etc/apt/apt.conf.d/use-local-proxy  
## add non-free packages  
RUN sed -i -e's/$/ non-free/' /etc/apt/sources.list  
  
RUN apt-get -qq update  
  
RUN apt-get -y install wget sudo  
  
# add mopidy repository  
RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -  
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list
http://apt.mopidy.com/mopidy.list  
  
RUN apt-get -qq update  
  
RUN apt-get -y install mopidy mopidy-spotify mopidy-alsamixer mopidy-scrobbler
gstreamer0.10-plugins-ugly  
  
WORKDIR /mopidy  
RUN mkdir sounds data  
  
RUN pip install Mopidy-Moped  
  
#  
RUN apt-get -y install supervisor cron  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY index-music.sh /etc/cron.daily/index-music.sh  
COPY mopidy.conf /mopidy/mopidy.conf  
  
CMD ["/usr/bin/supervisord"]  
  
#VOLUME ["/data"]  
# moped + web  
EXPOSE 6680  
# mpd  
EXPOSE 6600  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

