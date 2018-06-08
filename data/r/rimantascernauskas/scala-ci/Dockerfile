ARG tag=stable  
FROM debian:${tag}  
  
RUN apt-get update  
RUN apt-get install -y apt-utils apt-transport-https dialog apt-utils git
gnupg2 openjdk-8-jdk  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823  
RUN apt-get update  
RUN apt-get install sbt  
RUN sbt "clean"  
RUN rm -rf target

