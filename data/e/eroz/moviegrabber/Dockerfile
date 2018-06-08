FROM phusion/baseimage:0.9.11  
MAINTAINER eroz (rsanch1@gmail.com)  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables.  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
#ENV HOME /root  
# set sane localeRUN locale-gen en_US en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Correct user and group uid/guid  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /config nobody  
  
ADD sources.list /etc/apt/  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install unzip  
  
RUN apt-get install -qy python sqlite wget python-openssl  
  
# install application  
#####################  
# make destination folder  
RUN mkdir -p /opt/moviegrabber  
  
# download zip from github - url zip name is different to destination  
ADD https://github.com/binhex/moviegrabber/archive/master.zip
/opt/moviegrabber/moviegrabber-master.zip  
  
# unzip to folder  
RUN unzip /opt/moviegrabber/moviegrabber-master.zip -d /opt/moviegrabber/  
  
# move unzipped contents back to moviegrabber root  
RUN mv /opt/moviegrabber/moviegrabber-master/* /opt/moviegrabber/  
  
# remove files and folders  
RUN rm /opt/moviegrabber/moviegrabber-master.zip  
RUN rm -rf /opt/moviegrabber/moviegrabber-master/  
  
# docker settings  
#################  
# map /config to host defined config path (used to store configuration from
app)  
VOLUME ['/config']  
  
# map /downloads to host defined download path (used to store data from app)  
VOLUME ['/downloads']  
  
# map /movies to host defined movie path (used to read/write to media library)  
VOLUME ['/movies']  
  
# expose port for http  
EXPOSE 9191  
# set permissions  
#################  
# change owner  
RUN chown -R nobody:users /opt/moviegrabber  
RUN chmod -R 775 /opt/moviegrabber  
# add moviegrabber to runit  
###############  
RUN mkdir /etc/service/moviegrabber  
ADD moviegrabber.sh /etc/service/moviegrabber/run  
RUN chmod a+x /etc/service/moviegrabber/run  

