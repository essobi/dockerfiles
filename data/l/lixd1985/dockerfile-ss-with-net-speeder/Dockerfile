# shadowsocks-net-speeder  
FROM alpine:latest  
  
ENV SS_VERSION 2.8.2  
ENV GLIBC_VERSION 2.23-r3  
  
ENV INTERFACE eth0  
ENV METHOD aes-256-cfb  
ENV PASSWORD 123456  
ENV PORT 20080  
RUN apk add --no-cache bash git py-pip libnet libpcap libnet-dev libpcap-dev
gcc g++ supervisor  
  
RUN pip install shadowsocks==${SS_VERSION} supervisor-stdout  
  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
  
RUN mv net_speeder /usr/local/bin/  
RUN chmod +x /usr/local/bin/net_speeder  
  
RUN mkdir -p /etc/supervisor/conf.d/ /var/log/supervisor/  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 20080  
# Configure container to run as an executable  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

