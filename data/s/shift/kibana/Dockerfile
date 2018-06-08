FROM shift/ubuntu:15.04  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
RUN apt-get update \  
&& apt-get install --yes --force-yes wget npm \  
&& cd /opt \  
&& wget
https://download.elasticsearch.org/kibana/kibana/kibana-4.0.2-linux-x64.tar.gz
\  
&& tar xfvz kibana-4.0.2-linux-x64.tar.gz \  
&& mv kibana-4.0.2-linux-x64 kibana  
  
EXPOSE 5601  
ADD files/start.sh /start.sh  
  
ENTRYPOINT ["/start.sh"]  

