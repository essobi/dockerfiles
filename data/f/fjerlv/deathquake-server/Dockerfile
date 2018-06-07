FROM ubuntu:16.04  
MAINTAINER fjerlv@cs.au.dk  
  
RUN apt-get update  
RUN apt-get install -y wget libxml2 gawk  
  
WORKDIR /root/deathquake-server/  
  
# Download pak0.pk3 from a mirror  
RUN mkdir /root/deathquake-server/ioquake3  
RUN mkdir /root/deathquake-server/ioquake3/baseq3  
COPY download-pak0.sh /root/deathquake-server/download-pak0.sh  
COPY SHA256SUM /root/deathquake-server/SHA256SUM  
RUN chmod +x /root/deathquake-server/download-pak0.sh  
RUN /root/deathquake-server/download-pak0.sh  
  
RUN mv pak0.pk3 /root/deathquake-server/ioquake3/baseq3/pak0.pk3  
  
RUN wget http://ioquake3.org/files/1.36/installer/ioquake3-1.36-7.1.x86_64.run  
RUN wget http://ioquake3.org/files/1.36/data/ioquake3-q3a-1.32-9.run  
  
RUN mkdir /root/deathquake-server/tmp1  
RUN mkdir /root/deathquake-server/tmp2  
  
RUN chmod +x ioquake3-1.36-7.1.x86_64.run  
RUN chmod +x ioquake3-q3a-1.32-9.run  
  
RUN ./ioquake3-1.36-7.1.x86_64.run --tar xf -C /root/deathquake-server/tmp1  
RUN tar xf /root/deathquake-server/tmp1/ioquake3.x86_64.tar -C
/root/deathquake-server/ioquake3  
RUN ./ioquake3-q3a-1.32-9.run --tar xf -C /root/deathquake-server/tmp2  
RUN tar xf /root/deathquake-server/tmp2/idpatchpk3s.tar -C /root/deathquake-
server/ioquake3/baseq3/  
  
RUN rm -rf /root/deathquake-server/tmp1  
RUN rm -rf /root/deathquake-server/tmp2  
  
COPY baseq3/bots.cfg /root/deathquake-server/ioquake3/baseq3/bots.cfg  
COPY baseq3/server.cfg /root/deathquake-server/ioquake3/baseq3/server.cfg  
COPY start_server.sh /root/deathquake-server/start_server.sh  
RUN chmod +x /root/deathquake-server/start_server.sh  

