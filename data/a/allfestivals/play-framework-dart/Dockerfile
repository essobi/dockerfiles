FROM google/dart  
  
MAINTAINER Jakub Uhrik <jakuub@bookyourself.com>  
  
# ENV PLAY_VERSION 2.2.3  
ENV ACTIVATOR_VERSION 1.3.6  
# ENV PATH $PATH:/opt/play-$PLAY_VERSION  
ENV PATH $PATH:/opt/activator-dist-$ACTIVATOR_VERSION  
  
RUN apt-get update && apt-get install -y unzip openjdk-7-jdk  
# ADD http://downloads.typesafe.com/play/$PLAY_VERSION/play-$PLAY_VERSION.zip
/tmp/play-$PLAY_VERSION.zip  
ADD https://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip
/tmp/typesafe-activator-$ACTIVATOR_VERSION.zip  
# RUN (cd /opt && unzip /tmp/play-$PLAY_VERSION.zip && rm -f
/tmp/play-$PLAY_VERSION.zip)  
RUN (cd /opt && unzip /tmp/typesafe-activator-$ACTIVATOR_VERSION && \  
rm -f /tmp/typesafe-activator-$ACTIVATOR_VERSION.zip)  
  
WORKDIR /app  
EXPOSE 9000  
# Define default command.  
CMD ["bash"]  

