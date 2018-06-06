### Dockerfile for airvideohd  
### based on: https://github.com/dmaxwell351/docker-
containers/tree/master/airvideohd  
###  
FROM phusion/baseimage:0.9.16  
MAINTAINER hdo <huydo1@gmail.com>  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
CMD ["./airvideohd.sh"]  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Add h.265 repo  
RUN apt-add-repository ppa:strukturag/libde265  
  
# Install VLC  
RUN \  
apt-get update && \  
apt-get install -y vlc && \  
apt-get install -y wget && \  
apt-get install -y vlc-plugin-libde265 && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Set custom time zone  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Download AirVideoHD  
RUN wget -O /AirVideoServerHD-2.2.3.tar.bz2
"https://s3.amazonaws.com/AirVideoHD/Download/AirVideoServerHD-2.2.3.tar.bz2"  
  
# Decompress AirVideoHD  
RUN tar jxf /AirVideoServerHD-2.2.3.tar.bz2  
  
### Configure Service Startup  
COPY rc.local /etc/rc.local  
RUN chmod a+x /etc/rc.local && \  
mkdir -p /config/logs && \  
mkdir -p /config/ApplicationData && \  
cp -n /Server.properties /config/server.properties && \  
chown -R nobody:users /config && \  
mkdir /conversionPath && \  
chown -R nobody:users /conversionPath && \  
mkdir /videos && \  
chown -R nobody:users /videos  
  
# Copy default  
COPY airvideohd.sh /airvideohd.sh  
  
RUN chmod a+x airvideohd.sh  
  
EXPOSE 45633  
VOLUME ["/config", "/conversionPath", "/videos"]  
  
### END  

