FROM phusion/baseimage:0.9.22  
MAINTAINER Filechaser <dateirunner@gmail.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
RUN mkdir /etc/service/plex  
ADD plexinit.sh /etc/service/plex/run  
RUN chown root:root /etc/service/plex/run  
RUN chmod u+x /etc/service/plex/run  
  
# Update all base packages  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
#Plex als User 5000 erzwingen #User Plex zur Gruppe hinzufügen  
RUN adduser --system --home /var/lib/plexmediaserver --uid 5000 --group
--shell /bin/bash plex  
  
#ADD plexanalyze /etc/cron.d/plexanalyze  
#Installation von benötigten Files  
RUN apt-get update && apt-get install -qy \  
htop \  
git \  
vim \  
locales \  
curl \  
wget \  
rsync \  
python3 \  
python3-pip \  
speedtest-cli \  
udev  
RUN pip3 install requests  
  
#Plex und Plexscripts  
#RUN git clone https://github.com/Filechaser/scripts /plexscripts  
#RUN chown -R plex:plex /plexscripts  
#RUN git clone https://github.com/mrworf/plexupdate /plexupdate  
#RUN chown -R plex:plex /plexupdate  
#RUN /plexupdate/plexupdate.sh -p -a  
RUN curl -J -L -o /tmp/plex.deb https://downloads.plex.tv/plex-media-
server/1.8.1.4140-82ea538ca/plexmediaserver_1.8.1.4140-82ea538ca_amd64.deb  
#COPY /setupfile/setup.deb /tmp/plex.deb  
#Plex installieren  
RUN dpkg -i /tmp/plex.deb  
  
#Plex installationsfiles entfernen  
RUN rm /tmp/plex.deb  
  
#COPY /setupfile/setup.deb /tmp/plex.deb  
#RUN dpkg -i /tmp/plex.deb  
#Plex installationsfiles entfernen  
#RUN rm /tmp/plex.deb  
#Reparatur der Libraries #Reparatur des Paths  
RUN ln -s /usr/lib/plexmediaserver/lib* /usr/lib  
ENV PATH="/usr/lib/plexmediaserver:${PATH}"  
#Locales  
RUN locale-gen "en_US.UTF-8"  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
VOLUME ["/var/lib/plexmediaserver/"]  
EXPOSE 32400  
#Clean Installdirs  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

