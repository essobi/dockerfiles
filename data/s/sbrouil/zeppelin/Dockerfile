FROM debian:jessie  
  
WORKDIR /zeppelin  
  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
openjdk-7-jre \  
tar  
  
RUN wget
https://dist.apache.org/repos/dist/release/zeppelin/zeppelin-0.6.0/zeppelin-0.6.0-bin-
all.tgz \  
&& tar -xvf zeppelin-0.6.0-bin-all.tgz \  
&& mv ./zeppelin-0.6.0-bin-all/* .  
  
VOLUME ["/zeppelin/notebook", "/zeppelin/logs"]  
CMD /zeppelin/bin/zeppelin-daemon.sh start && /bin/bash  

