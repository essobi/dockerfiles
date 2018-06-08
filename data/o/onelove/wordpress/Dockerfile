FROM debian:jessie  
MAINTAINER Goran Mekić <meka@lugons.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD . /app  
RUN /app/bin/build.sh  
CMD /app/bin/run.sh  
  
VOLUME /var/www  
EXPOSE 9000  

