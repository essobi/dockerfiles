FROM debian:latest  
MAINTAINER wagner.roncoletta@gmail.com  
  
  
# make sure the package repository is up to date and update ubuntu  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade  
RUN apt-get install -y wget  
  
ENV HOME /root  
  
# supervisor installation &&  
# create directory for child images to store configuration in  
RUN apt-get -y install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
# supervisor base configuration  
ADD supervisor.conf /etc/supervisor.conf  
  
# default command  
CMD ["supervisord", "-c", "/etc/supervisor.conf"]  
  

