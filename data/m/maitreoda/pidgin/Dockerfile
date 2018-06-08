FROM debian:latest  
  
MAINTAINER Maitre Oda  
  
RUN apt-get update  
RUN apt-get install -y pidgin pidgin-otr tor privoxy ca-certificates  
  
RUN echo "SocksPort localhost:9050" >> /etc/tor/torrc  
  
RUN echo "forward-socks5 / localhost:9050 ." >> /etc/privoxy/config  
RUN echo "forward-socks4 / localhost:9050 ." >> /etc/privoxy/config  
RUN echo "forward-socks4a / localhost:9050 ." >> /etc/privoxy/config  
  
RUN update-rc.d -f tor remove  
RUN update-rc.d -f tor defaults  
RUN update-rc.d -f tor enable  
RUN update-rc.d -f privoxy remove  
RUN update-rc.d -f privoxy defaults  
RUN update-rc.d -f privoxy enable  
  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get --purge autoremove -y  
  
EXPOSE 8118 9050 5222  
CMD pidgin -f  

