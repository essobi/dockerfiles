FROM openjdk:8-jre  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
RUN apt-get update  
RUN apt-get install -y sbt=0.13.15.3  
RUN mkdir -p /home/build  
VOLUME /home/build  
WORKDIR /home/build  

