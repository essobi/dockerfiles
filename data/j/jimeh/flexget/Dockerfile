FROM ubuntu:16.04  
MAINTAINER jimeh  
  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
# define what version of flexget to install  
ENV FLEXGET_VERSION 2.5.1  
RUN mkdir /scripts  
  
# install everything  
ADD install.sh /scripts/  
RUN chmod +x /scripts/install.sh  
RUN /scripts/install.sh  
  
# add init script  
ADD init.sh /scripts/init.sh  
RUN chmod +x /scripts/init.sh  
  
# add default config file  
RUN mkdir /templates  
ADD config.example.yml /templates/  
  
# used to store flexget config files  
VOLUME /config  
WORKDIR /config  
  
# use /data in your flexget config.yml file for input/output of files  
VOLUME /data  
  
# expose port for flexget webui  
EXPOSE 3539  
# init script sets uid, gid, permissions and launches flexget  
CMD ["/scripts/init.sh"]  

