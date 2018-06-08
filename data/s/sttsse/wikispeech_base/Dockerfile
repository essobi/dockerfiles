## 1. BASICS  
# STARTING FROM THE OFFICIAL GOLANG IMAGE (required by pronlex)  
FROM golang  
  
# META/LABELS  
LABEL "se.stts.vendor"="STTS - Speech technology services - http://stts.se"  
  
# SET UP APT  
RUN apt-get update -y && apt-get upgrade -y && apt-get install apt-utils -y  
  
# INSTALL DEBUGGING/DEV TOOLS  
RUN apt-get install -y libnet-ifconfig-wrapper-perl/stable curl wget emacs  
  
## 2. DEPENDENCIES  
####### COMMON DEPS  
RUN apt-get install -y git  
  
####### WIKISPEECH SERVER/MOCKUP DEPS  
RUN apt-get install -y opus-tools python3-pip netcat  
RUN pip3 install simplejson requests flask flask_cors pytz tzlocal  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
####### PRONLEX DEPS  
RUN apt-get install -y sqlite3 gcc build-essential  
  
####### MARYTTS DEPS  
# PYTHON  
RUN apt-get install -y python  
  
# JAVA 8  
RUN apt-get install -y software-properties-common && add-apt-repository
ppa:openjdk && apt-get install -y openjdk-8-jdk  
  
####### PATHS  
RUN mkdir -p /wikispeech  
RUN mkdir -p /wikispeech/bin  
#RUN export PATH=/wikispeech/bin:$PATH # doesn't work  
###### BUILD INFO  
RUN mkdir -p /wikispeech  
WORKDIR /wikispeech  
ENV BUILD_INFO_FILE /wikispeech/.wikispeech_base_build_info.txt  
RUN git clone https://github.com/stts-se/wikispeech_compose.git  
WORKDIR /wikispeech/wikispeech_compose  
RUN echo "Application name: wikispeech_base" >> $BUILD_INFO_FILE  
RUN echo -n "Build timestamp: " >> $BUILD_INFO_FILE  
RUN date --utc "+%Y-%m-%d %H:%M:%S %Z" >> $BUILD_INFO_FILE  
RUN echo "Built by: docker" >> $BUILD_INFO_FILE  
RUN echo -n "Git release: " >> $BUILD_INFO_FILE  
RUN git describe --tags >> $BUILD_INFO_FILE || echo "undefined" >>
$BUILD_INFO_FILE  
  
WORKDIR "/"  

