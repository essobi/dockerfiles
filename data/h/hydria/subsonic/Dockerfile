#Subsonic StandAlone Docker Image v6.1.3  
FROM ubuntu:16.04  
MAINTAINER Hydria  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8 ENV LC_ALL en_US.UTF-8  
RUN echo "Subsonic StandAlone Docker Image With FFMPEG (v6.0)"  
RUN apt-get update  
RUN apt-get install locales ffmpeg libav-tools openjdk-8-jre-headless nano
flac lame wget -y  
RUN mkdir -p /opt/subsonic && locale-gen "en_US.UTF-8"  
RUN wget -qO- https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-6.1.3-standalone.tar.gz | tar xvz -C /opt/subsonic  
RUN mkdir -p /var/subsonic/transcode && \  
cd /var/subsonic/transcode && \  
ln -s "$(which ffmpeg)"  
  
VOLUME ["/var/music", "/var/subsonic"]  
EXPOSE 4040  
CMD /bin/bash -c "export LANG=en_US.UTF-8 && /opt/subsonic/subsonic.sh &&
/bin/bash"  

