# make tsdbrelay image  
FROM ubuntu:14.04.3  
MAINTAINER cheon <cheon119950317@gmail.com>  
RUN mkdir /opt/tsdbrelay  
RUN apt-get update  
RUN apt-get -y install curl  
RUN curl -o /opt/tsdbrelay/tsdbrelay-linux-amd64 -L "https://github.com/bosun-
monitor/bosun/releases/download/0.5.0/tsdbrelay-linux-amd64"  
ADD startTsdbrelay.sh /opt/tsdbrelay/startTsdbrelay.sh  
ADD stopTsdbrelay.sh /opt/tsdbrelay/stopTsdbrelay.sh  
Add setEnv /setEnv  
RUN chmod +x /opt/tsdbrelay/startTsdbrelay.sh /opt/tsdbrelay/stopTsdbrelay.sh
/opt/tsdbrelay/tsdbrelay-linux-amd64 /setEnv  
EXPOSE 5252  
CMD /setEnv && /opt/tsdbrelay/startTsdbrelay.sh && tail -f
/opt/tsdbrelay/run.log  

