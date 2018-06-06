#######################################################  
# This dockerfile builds chilli #  
# #  
# Author: Demon Tsai #  
# Repository: demontsai/coovachilli:1.3.0 #  
# Version: 1.0 #  
# #  
#######################################################  
  
FROM demontsai/ubuntu64:14.04  
  
MAINTAINER Demon Tsai demontsai@estinet.com  
  
  
##### Update system and install apps  
RUN apt-get update -qq  
RUN apt-get install -qqy iptables libssl-dev devscripts haserl debhelper  
  
##### Environment  
ENV CHILLI_VERSION 1.3.0  
ENV CHILLI_URL https://coova.github.io/coova-chilli/coova-
chilli-$CHILLI_VERSION.tar.gz  
  
##### Install chilli  
WORKDIR /root  
RUN wget $CHILLI_URL  
RUN tar xzvf coova-chilli-$CHILLI_VERSION.tar.gz  
WORKDIR coova-chilli-$CHILLI_VERSION  
RUN debuild -b -us -uc  
RUN dpkg -i ../*.deb  
WORKDIR /root  
RUN sed -i 's/START_CHILLI=0/START_CHILLI=1/1' /etc/default/chilli  
RUN sed -i 's/DAEMON -- -c/DAEMON -- -f -d -c/1' /etc/init.d/chilli  
COPY chilli_cfg /usr/sbin/  
COPY chilli_init /usr/sbin/  
RUN echo "service chilli start" >> $ENTRYPOINT  
  
#EXPOSE 18120/udp 1812/udp 1813/udp  
  
##### Clean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/*chilli*  
  
#ENTRYPOINT $ENTRYPOINT  
  

