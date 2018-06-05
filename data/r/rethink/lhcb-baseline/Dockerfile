FROM rethink/testbed-baseline  
  
MAINTAINER robert.ende@fokus.fraunhofer.de  
  
#RUN apt-get -y install software-properties-common  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-
common  
  
#RUN add-apt-repository ppa:openjdk-r/ppa  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:openjdk-r/ppa  
  
RUN apt-get update -y && apt-get install -y git maven openjdk-8-jdk  
  
RUN apt-get remove -y openjdk-7-jre openjdk-7-jdk  
  
RUN update-java-alternatives -s java-1.8.0-openjdk-amd64  
  
RUN cd /opt/reTHINK/ && git clone https://github.com/reTHINK-project/dev-qos-
support  
  
RUN cd /opt/reTHINK/dev-qos-support/lhcb/ && mvn clean install  
  
ENTRYPOINT ["echo", "This image (rethink/lhcb-baseline) is not intended to be
invoked directly. If you derived your own image, you will need to specify a
docker ENTRYPOINT."]

