FROM ubuntu:latest  
MAINTAINER Nicolas Limage <github@xephon.org>  
ENV NSD_CONFDIR /etc/nsd  
ENV NSD_RUNDIR /run/nsd  
ENV NSD_ZONESDIR $NSD_CONFDIR/zones  
VOLUME $NSD_ZONESDIR  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y install
nsd  
RUN mkdir $NSD_RUNDIR && chown nsd:nsd $NSD_RUNDIR  
COPY nsd.conf $NSD_CONFDIR/nsd.conf  
COPY nsd-reload nsd-genzoneconf nsd-start /usr/local/bin/  
RUN chmod 755 /usr/local/bin/nsd-*  
EXPOSE 53/udp 53/tcp  
CMD ["/usr/local/bin/nsd-start"]  

