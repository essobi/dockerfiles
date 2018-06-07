FROM ubuntu:14.04.1  
MAINTAINER eltimn  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV APT_GET_UPDATE 2014-09-11_1  
ENV JETTY_VERSION 9.2.2.v20140723  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y  
  
# Install Java  
RUN apt-get install -y wget openjdk-7-jre  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install Jetty  
RUN wget http://download.eclipse.org/jetty/${JETTY_VERSION}/dist/jetty-
distribution-${JETTY_VERSION}.tar.gz -O /tmp/jetty.tar.gz  
RUN tar xv -C /opt --file /tmp/jetty.tar.gz  
RUN ln -s /opt/jetty-distribution-${JETTY_VERSION} /opt/jetty  
RUN rm /tmp/jetty.tar.gz  
  
WORKDIR /opt/jetty  
  
EXPOSE 8080  
CMD ["java", "-jar", "start.jar"]  

