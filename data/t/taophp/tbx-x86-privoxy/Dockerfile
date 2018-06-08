# TreasureBox base Dockerfile for images  
#  
# Version 0.0.1  
FROM debian  
  
MAINTAINER BrokenClock "stephane.mourey@impossible-exil.info"  
RUN set ENV_DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update  
RUN apt-get install -y privoxy  
  
RUN sed -e 's/^listen-address localhost:8118.*/listen-address :8118/'
/etc/privoxy/config >/etc/privoxy/config.new  
  
RUN rm /etc/privoxy/config && mv /etc/privoxy/config.new /etc/privoxy/config  
  
RUN printf "{-deanimate-gifs}\n{+filter{unsolicited-
popups}}\n{+filter{banners-by-
link}}\n{+filter{google}}\n{+filter{yahoo}}\n{+filter{msn}}\n"
>>/etc/privoxy/user.action  
  
EXPOSE 8118  
CMD ["/usr/sbin/privoxy","--no-daemon","/etc/privoxy/config"]  
  

