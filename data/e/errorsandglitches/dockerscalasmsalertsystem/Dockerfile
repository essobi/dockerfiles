FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository ppa:webupd8team/java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN apt-get update && apt-get install -y oracle-java8-installer  
  
RUN apt-get update && apt-get install -y unzip && \  
apt-get install -y apt-transport-https  
  
ENV PROJECT_HOME /usr/src  
  
RUN mkdir -p $PROJECT_HOME/sbt $PROJECT_HOME/app  
  
ENV SBT_VERSION 1.0.1  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823  
RUN apt-get update && apt-get install -y sbt=$SBT_VERSION  
  
COPY . $PROJECT_HOME/app  
WORKDIR $PROJECT_HOME/app  
EXPOSE 9000  
RUN sbt compile -v  
CMD ["sbt", "--version"]  
  

