FROM phusion/baseimage:latest  
MAINTAINER needo <sensei73@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
# Install Dependencies  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty
universe multiverse" \  
&& add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" \  
&& apt-get update -q \  
&& apt-get install -qy python git \  
&& apt-get clean  
  
# Install CouchPotato  
RUN mkdir /opt/couchpotato \  
&& git clone https://github.com/RuudBurger/CouchPotatoServer.git
/opt/couchpotato \  
&& chown -R nobody:users /opt/couchpotato  
  
EXPOSE 5050  
# Couchpotato Configuration  
VOLUME /config  
  
# Downloads directory  
VOLUME /downloads  
  
# Movies directory  
VOLUME /movies  
  
# Add edge.sh to execute during container startup & Add CouchPotato to runit  
RUN mkdir -p /etc/my_init.d \  
&& mkdir /etc/service/couchpotato  
ADD edge.sh /etc/my_init.d/edge.sh  
ADD couchpotato.sh /etc/service/couchpotato/run  
RUN chmod +x /etc/my_init.d/edge.sh \  
&& chmod +x /etc/service/couchpotato/run  

