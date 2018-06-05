FROM ubuntu:14.04  
MAINTAINER Sean Anastasi "sean@anasta.si"  
RUN apt-get update \  
&& apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java \  
&& add-apt-repository -y ppa:bubbleguuum/bubbleupnpserver  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get update \  
&& apt-get install -y oracle-java8-installer bubbleupnpserver  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
EXPOSE 58050/tcp 58051/tcp 1900/udp  
  
ENTRYPOINT ["/usr/share/bubbleupnpserver/launch.sh"]  
  

