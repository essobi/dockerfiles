FROM ubuntu:bionic  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# apt-utils seems missing and warnings are shown, so we install it.  
RUN apt-get update -q -q && \  
apt-get install --yes \--force-yes apt-utils tzdata locales file sudo && \  
echo 'UTC' > /etc/timezone && \  
rm /etc/localtime && \  
dpkg-reconfigure tzdata && \  
apt-get upgrade --yes \--force-yes && \  
rm -f /etc/cron.weekly/fstrim  

