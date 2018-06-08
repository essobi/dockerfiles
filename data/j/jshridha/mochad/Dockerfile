FROM phusion/baseimage  
  
RUN \  
apt-get update && \  
apt-get install -y cmake apt-utils build-essential && \  
apt-get install -y libusb-1.0-0-dev supervisor && \  
apt-get clean -y && \  
rm -rf /usr/share/locale/* && \  
rm -rf /usr/share/man/* && \  
rm -rf /tmp/*  
  
# Define working directory.  
WORKDIR /root  
  
ADD mochad-0.1.16.tar.gz /root/  
  
RUN \  
cd mochad-0.1.16 && ./configure && make && make install && rm -rf /root/*  
  
ADD *.conf /etc/supervisor/conf.d/  
  
ADD services/ /etc/service/  
#RUN chmod -v +x /etc/service/*/run /etc/service/*/finish /etc/my_init.d/*.sh  
RUN chmod -v +x /etc/service/*/run  

