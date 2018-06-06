FROM nginx:1.11  
  
MAINTAINER Bertrand Roussel "bertrand.roussel@cor-net.org"  
RUN apt-get update && \  
apt-get install -y dnsmasq  
  
RUN echo "\n\n# Docker extra config \nuser=root\naddn-hosts=/etc/hosts\n" >>
/etc/dnsmasq.conf  
  
EXPOSE 80 443  
  
CMD service dnsmasq restart && nginx -g "daemon off;"  

