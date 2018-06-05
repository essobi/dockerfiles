# create bosun image  
FROM ubuntu:14.04.3  
MAINTAINER cheon <cheon19950317@gmail.com>  
RUN mkdir /opt/bosun  
RUN apt-get update  
RUN apt-get -y install curl  
RUN curl -o /opt/bosun/bosun-linux-amd64 -L "https://github.com/bosun-
monitor/bosun/releases/download/0.5.0/bosun-linux-amd64"  
RUN chmod +x /opt/bosun/bosun-linux-amd64  
ADD bosun.conf /opt/bosun/bosun.conf  
ADD startBosun.sh /opt/bosun/startBosun.sh  
ADD stopBosun.sh /opt/bosun/stopBosun.sh  
ADD setEnv /setEnv  
RUN chmod +x /opt/bosun/startBosun.sh /opt/bosun/stopBosun.sh /setEnv  
EXPOSE 8070  
CMD /setEnv && /opt/bosun/startBosun.sh && touch /opt/bosun/run.log && tail -f
/opt/bosun/run.log  

