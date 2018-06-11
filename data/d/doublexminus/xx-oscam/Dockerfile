FROM doublexminus/xx-ubuntu14.04-s6-base  
MAINTAINER DoubleXMinus <doublexminus@web.de>  
  
WORKDIR /tmp  
  
RUN apt-get update  
RUN apt-get install -y wget subversion make build-essential cmake vim libssl-
dev libpcsclite1 libpcsclite-dev dialog libudev-dev libusb-1.0.0-dev  
  
RUN svn co http://www.streamboard.tv/svn/oscam/trunk oscam-svn  
RUN cd oscam-svn  
RUN mkdir build  
RUN cd build  
RUN cmake ./oscam-svn/  
RUN make && make install  
RUN mkdir /var/log/oscam  
RUN touch /var/log/oscam/oscam.log  
  
COPY /config/basic/bootoscam.sh /etc/services.d/oscam/run  
COPY /config/basic/shutdownoscam.sh /etc/services.d/oscam/finish  
COPY /config/basic/rsyslog.sh /etc/services.d/rsyslog/run  
# add configs  
COPY /config/basic/rsyslog.conf /etc/  
  
EXPOSE 2000 8888  
VOLUME /config  
  
ENTRYPOINT ["/init"]

