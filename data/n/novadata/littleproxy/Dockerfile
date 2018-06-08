#  
# Java 1.7 & Maven & LittleProxy Dockerfile  
#  
# https://github.com/fivesmallq/littleproxy-docker  
#  
# pull base image.  
FROM dockerfile/java:oracle-java7  
  
# maintainer details  
MAINTAINER Wu ZhiQiang "fivesmallq@gmail.com"  
# update packages and install maven  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y vim wget curl git maven  
  
# attach volumes  
VOLUME /volume/git  
  
# create working directory  
RUN mkdir -p /local/git  
WORKDIR /local/git  
  
# run LittleProxy  
CMD git clone git://github.com/adamfisk/LittleProxy.git  
  
EXPOSE 8080  
ENTRYPOINT [\  
"/local/git/LittleProxy/run.bash" \  
]

