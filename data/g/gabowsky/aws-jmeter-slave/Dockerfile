FROM cirit/jmeter:base  
  
MAINTAINER Gabor Rendes <rendesg@gmail.com>  
  
ENV STARTUP_HOME=/usr/local/docker-jmeter-slave  
ENV PATH=${STARTUP_HOME}:${PATH}  
  
RUN apt-get -qq update  
  
RUN apt-get -qq -y install wget  
RUN apt-get -qq -y install curl  
  
RUN mkdir $STARTUP_HOME  
  
RUN wget -P $STARTUP_HOME https://raw.githubusercontent.com/rendesg/docker-
aws-jmeter-slave/master/startup  
  
RUN chmod 755 $STARTUP_HOME/startup  
  
EXPOSE 60000  
ENTRYPOINT ["startup"]

