FROM debian:jessie  
MAINTAINER korjavin@gmail.com  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update &&
DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata ssmtp cron net-tools
vim-tiny  
  
#RUN echo Asia/Yekaterinburg > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  

