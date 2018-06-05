FROM ubuntu:latest  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-
common curl vim  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:webupd8team/java
&& apt-get -y update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-
set-selections && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java7-installer  
  
ADD http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/0.13.5/sbt-launch.jar /opt/sbt/  
ADD sbt /opt/sbt/bin/  
ENV PATH /opt/sbt/bin:$PATH  
  
WORKDIR /data  
ENTRYPOINT ["sbt"]  
CMD ["--help"]  

