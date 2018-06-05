From trumanz/ubuntu14.04-dev  
maintainer Truman Zhou <truman.ck.zhou@gmail.com>  
  
RUN wget -nv http://public-
repo-1.hortonworks.com/ambari/ubuntu14/2.x/updates/2.2.0.0/ambari.list -O
/etc/apt/sources.list.d/ambari.list \  
&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD \  
&& apt-get update \  
&& apt-get install -y ambari-server ambari-agent  
  
RUN rm -f /root/.ssh/*  
COPY ssh/* /root/.ssh/  
  

