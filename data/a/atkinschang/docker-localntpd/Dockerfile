FROM atkinschang/docker-baseimage:latest-base  
MAINTAINER Atkins Chang "atkinschang@icloud.com"  
ADD . /build  
  
RUN apt-get update && apt-get install -y --no-install-recommends ntp && cp
/build/ntp.conf /etc/ntp.conf && cp /build/ntpdate /etc/cron.hourly/ntpdate &&
mv /build/ntp /etc/my_init.d/ && apt-get clean && rm -rf /build && rm -rf
/var/lib/apt/lists/*  
  
CMD ["/sbin/my_init"]  

