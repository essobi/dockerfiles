FROM ubuntu:15.10  
MAINTAINER Cuteribs <ericfine1981@live.com>  
  
  
RUN apt-get install -y libssl1.0.0 init-system-helpers lib32z1 logrotate
libpopt0 cron  
ADD ./packages/xware.tar.gz /app/  
COPY ./packages/*.deb /app/  
COPY ./*.sh /app/  
RUN chmod +x /app/*.sh  
  
# Install xware  
RUN chmod +x /app/xware/portal  
VOLUME /app/TDDOWNLOAD  
  
# Install shadowsocks-libev  
RUN dpkg -i /app/shadowsocks-libev_2.4.6-1_amd64.deb  
RUN rm /app/shadowsocks-libev_2.4.6-1_amd64.deb  
RUN rm /etc/init.d/shadowsocks-libev  
  
# Install privoxy  
RUN dpkg -i /app/privoxy_3.0.23-3_amd64.deb  
RUN rm /app/privoxy_3.0.23-3_amd64.deb  
RUN rm /etc/init.d/privoxy  
  
WORKDIR /app  

