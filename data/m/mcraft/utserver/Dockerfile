FROM ubuntu:13.04  
MAINTAINER manjula.ellawala@gmail.com  
  
RUN sed -i "s|archive|old-releases|" /etc/apt/sources.list  
RUN apt-get update -y && apt-get install wget unzip -y && apt-get clean all  
RUN wget http://download-
new.utorrent.com/os/linux-x64-ubuntu-13-04/track/beta/endpoint/utserver/ -O
/tmp/utserver.tar.gz \  
&& tar xzvf /tmp/utserver.tar.gz -C /opt && rm -f /tmp/utserver.tar.gz  
RUN mv /opt/utorrent-server-alpha-v3_3 /opt/utorrent  
RUN unzip /opt/utorrent/webui.zip -d /opt/utorrent/  
RUN mkdir /opt/downloads  
#RUN ln -sf /usr/share/zoneinfo/Asia/Colombo /etc/localtime  
VOLUME /opt/downloads  
WORKDIR /opt/utorrent  
EXPOSE 8080  
CMD ["./utserver"]  

