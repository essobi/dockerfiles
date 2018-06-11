FROM google/debian:wheezy  
MAINTAINER Jordan Li  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl tar wget unzip ca-certificates
openjdk-7-jre supervisor python2.7 && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV H2O_DOWNLOAD_URL http://h2o-release.s3.amazonaws.com/h2o/rel-
simons/4/h2o-3.0.1.4.zip  
ENV H2O_VERSION 3.0.1.4  
RUN wget "${H2O_DOWNLOAD_URL}" -O /opt/h2o-${H2O_VERSION}.zip --no-check-
certificate  
RUN cd /opt && unzip h2o-${H2O_VERSION}.zip && rm -rf h2o-${H2O_VERSION}.zip  
WORKDIR /opt/h2o-${H2O_VERSION}  
CMD ["java","-jar","h2o.jar"]  

