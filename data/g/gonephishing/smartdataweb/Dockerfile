############################################  
## Smart Data Web Framework ##  
############################################  
  
# Set base image as ubuntu  
FROM ubuntu:14.04  
MAINTAINER gonephishing <riteshoneinamillion@gmail.com>  
  
# Update and install necessary tools  
RUN echo "Force update cache"  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update  
RUN apt-get install -y maven  
RUN apt-get install -y wget  
RUN apt-get install -y git  
RUN apt-get install -y unzip  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
RUN apt-get install -y oracle-java8-installer && rm -rf /var/lib/apt/lists/*
&& rm -rf /var/cache/oracle-jdk8-installer  
RUN ["java", "-version"]  
  
# Get the flink release from github and build it on the image  
#RUN git clone https://github.com/apache/flink.git  
#WORKDIR flink/  
#RUN tools/change-scala-version.sh 2.11  
#RUN ["mvn", "clean", "install", "-DskipTests=true",
"-Dmaven.javadoc.skip=true", "-Dscala.version=2.11.4"]  
  
# Get the Smart data web framework from github and build it using maven  
RUN git clone https://github.com/gone-phishing/SDW.git  
WORKDIR SDW/  
RUN ["mvn", "clean", "install", "-Dmaven.test.skip=true"]  
#RUN java -cp ".:target/sdw-1.0.jar:./lib/*" org.sdw.Main  
  

