#  
# A dockerfile to run Oracle JRE and access it through the browser with noVNC.  
# Inspired by:  
# https://github.com/dockerfile/java/tree/master/oracle-java8  
#  
# BUILD DOCKER: docker build -t toastie/x11-novnc-oraclejre .  
# RUN DOCKER: docker run -it -p 8080:8080 toastie/x11-novnc-oraclejre  
# TEST DOCKER: docker exec -it -p 8080:8080 toastie/x11-novnc-oraclejre
/bin/bash  
FROM toastie/x11-novnc  
MAINTAINER toastie <user@example.com>  
  
# Expose Port.  
EXPOSE 8080  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV TZ Europe/Berlin  
  
  
# Install Java.  
RUN \  
apt-get install -y apt-utils software-properties-common \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update && apt-get install -y oracle-java8-installer oracle-
java8-set-default \  
&& apt-get clean  
  
# Run supervisor  
CMD ["/usr/bin/supervisord"]  

