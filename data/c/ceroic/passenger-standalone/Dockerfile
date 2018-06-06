FROM node:0.12-wheezy  
MAINTAINER Ceroic <ops@ceroic.com>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7  
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates
procps  
RUN echo "deb https://oss-binaries.phusionpassenger.com/apt/passenger wheezy
main" >> /etc/apt/sources.list.d/passenger.list  
RUN chown root: /etc/apt/sources.list.d/passenger.list  
RUN chmod 600 /etc/apt/sources.list.d/passenger.list  
RUN apt-get update  
RUN apt-get install -y passenger  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 3000  
CMD ["passenger", "start"]  

