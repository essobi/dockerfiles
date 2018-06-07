FROM debian:jessie  
  
LABEL maintainer "socketz@gmail.com"  
  
ENV TS_VERSION LATEST  
ENV LANG C.UTF-8  
ENV TS_DATA=/data  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install bzip2 wget ca-
certificates python3 \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -M -s /bin/false \--uid 1000 teamspeak3 \  
&& mkdir $TS_DATA  
  
ADD scripts/get-version.py /get-version  
ADD scripts/start-teamspeak3.sh /start-teamspeak3  
  
ADD data/* $TS_DATA/  
  
RUN chown -R teamspeak3:teamspeak3 $TS_DATA  
  
EXPOSE 9987/udp 10011 30034  
USER teamspeak3  
VOLUME $TS_DATA  
WORKDIR $TS_DATA  
  
CMD ["/start-teamspeak3"]  

