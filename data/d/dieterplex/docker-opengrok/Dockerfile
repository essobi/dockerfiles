#FROM ubuntu:16.04  
FROM dieterplex/docker-opengrok:0.12  
MAINTAINER Dieter Hsu "dieterplex@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
ENV OPENGROK_INSTANCE_BASE /opengrok  
ENV TERM xterm-color  
  
RUN apt update && apt install -y --no-install-recommends ant openjdk-8-jdk-
headless  
  
# install prebuild dist  
#COPY opengrok-0.13.tar.gz /tmp/  
#RUN mkdir /opengrok && tar zxvf /tmp/opengrok-0.13.tar.gz -C /opengrok
--strip-components=1  
# add perforce binary  
#ADD http://filehost.perforce.com/perforce/r15.2/bin.linux26x86_64/p4
/usr/local/bin/p4  
#RUN chmod +x /usr/local/bin/p4  
# install from latest source  
RUN rm -rf /opengrok/* && \  
curl -Lo - http://github.com/OpenGrok/OpenGrok/archive/master.tar.gz | tar
zxvf - -C /tmp/ && \  
ant -Dversion=latest -f /tmp/OpenGrok-master/build.xml dist && \  
tar zxvf /tmp/OpenGrok-master/dist/opengrok-latest.tar.gz -C /opengrok
--strip-components=1  
  
RUN apt purge ant -y openjdk-8-jdk-headless \  
&& apt clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD run.sh /rungrok  
ENTRYPOINT ["/rungrok"]  
  
EXPOSE 8080  

