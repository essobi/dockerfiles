FROM webdizz/baseimage-java8  
  
MAINTAINER Izzet Mustafaiev "izzet@mustafaiev.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV GATLING_VERSION 2.2.3  
RUN apt-get update && apt-get install -y unzip && apt-get clean \  
&& curl --progress-bar -v -sLo gatling-charts-highcharts-
bundle-${GATLING_VERSION}-bundle.zip
https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-
highcharts-bundle/${GATLING_VERSION}/gatling-charts-highcharts-
bundle-${GATLING_VERSION}-bundle.zip \  
&& unzip gatling-charts-highcharts-bundle-${GATLING_VERSION}-bundle.zip -d
/tmp \  
&& mv /tmp/gatling-charts-highcharts-bundle-${GATLING_VERSION} /opt/gatling \  
&& rm gatling-charts-highcharts-bundle-${GATLING_VERSION}-bundle.zip \  
&& apt-get remove -y --purge unzip \  
&& apt-get autoremove -y gir1.2-glib-2.0 gsfonts libdbus-glib-1-2 libfontenc1
libfreetype6 libgirepository-1.0-1 libxfont1 python-pycurl python3-apt
python3-dbus python3-gi python3-pycurl unattended-upgrades  
  
ENV PATH $PATH:/opt/gatling/bin  

