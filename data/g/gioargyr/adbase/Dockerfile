###############################  
# Dockerfile for SC7-Pilot #  
# BigDataEurope, Horizon2020 #  
# #  
# java 1.8.0_151 #  
# maven 3.0.5 #  
# tomcat 8.0.23 #  
# python elevation #  
# spark 1.6.2 #  
###############################  
  
FROM gioargyr/iplcppgdal:1.0.0  
  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
ENV PORT 8080  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.0.23  
  
  
# INSTALL PREREQUISITIES  
RUN apt-get update \  
&& apt-get install -y maven \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## INSTALLATION OF PYTHON-RELATED PREREQS  
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable \  
&& apt update \  
&& apt install -y gdal-bin python-gdal python3-gdal  
  
# elevation python module for downloading dems  
RUN apt install -y python3-pip \  
&& pip install --upgrade pip \  
&& pip install elevation \  
&& pip3 install --upgrade pip \  
&& pip3 install shapely  
  
  
# JAVA8-INSTALLATION  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt update \  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections \  
&& apt install -y oracle-java8-installer  
  
  
# INSTALL TOMCAT  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz \  
&& wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - \  
&& tar zxf apache-tomcat-*.tar.gz \  
&& rm apache-tomcat-*.tar.gz \  
&& mv apache-tomcat* tomcat  
  
  
# INSTALL SPARK  
RUN apt-get update \  
&& wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.2-bin-hadoop2.6.tgz \  
&& tar -xvzf spark-1.6.2-bin-hadoop2.6.tgz \  
&& mv spark-1.6.2-bin-hadoop2.6 spark \  
&& rm spark-1.6.2-bin-hadoop2.6.tgz \  
&& apt-get install -y libgfortran3  
  
  
ADD runtomcat.sh /runtomcat.sh  
  
RUN chmod +x /*.sh  
  
EXPOSE $PORT  
  
CMD ["/bin/bash", "/runtomcat.sh"]

