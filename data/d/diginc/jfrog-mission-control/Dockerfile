FROM frolvlad/alpine-oraclejdk8:slim  
  
ENV MC_VERSION 1.1  
ENV MC_SHA256 88f7774b0a54fcc6cf8c44cf5627d3e719b1d8b80f78cab0ab478182d414e29e  
  
RUN apk add --update bash wget ca-certificates && \  
wget -q -O jfrog-mission-control.zip
https://bintray.com/artifact/download/jfrog/jfrog-mission-control/jfrog-
mission-control-$MC_VERSION.zip?agree=true && \  
echo "$MC_SHA256 jfrog-mission-control.zip" | sha256sum -c - && \  
unzip jfrog-mission-control.zip && \  
mv mission-control-*/ /home/mission-control/ && \  
rm jfrog-mission-control.zip && \  
rm /var/cache/apk/*  
  
ENTRYPOINT /home/mission-control/bin/mission-control.sh  

