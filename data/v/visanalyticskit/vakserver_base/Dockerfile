FROM visanalyticskit/vakserver_phusion:0.9.18  
MAINTAINER visanalyticskit@gmail.com  
  
ENV TERM=dumb \  
MY_TZ=Europe/Berlin  
  
RUN echo $MY_TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
&& mkdir /tz && \  
cp /etc/timezone /tz/ && cp /etc/localtime /tz/ && \  
apt-get update && DEBIAN_FRONTEND=noninteractive && \  
apt-get install -yq --no-install-recommends \  
git \  
wget && \  
  
apt-get autoclean && apt-get autoremove && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

