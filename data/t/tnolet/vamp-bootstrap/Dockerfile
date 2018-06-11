# Install basics for Vert.x container  
FROM ubuntu:latest  
  
MAINTAINER Tim Nolet  
  
RUN apt-get install -y software-properties-common  
  
RUN apt-get update -y  
  
RUN apt-get install -y --no-install-recommends openjdk-7-jre  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
RUN apt-get install -y curl  
  
EXPOSE 80  
EXPOSE 5701  
EXPOSE 5702  
RUN curl -sL https://s3-eu-
west-1.amazonaws.com/deploy.magnetic.io/snapshots/vamp-bootstrap-1.1.tar.gz |
tar -xz  
  
ENTRYPOINT ["vamp-bootstrap-1.1/bin/cluster_boot.sh"]  
  
CMD ["vamp-agent-0.1.0"]

