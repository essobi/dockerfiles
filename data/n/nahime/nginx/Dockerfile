FROM nahime/dotdeb  
MAINTAINER Vincenzo Petrucci (nahime)  
ENV DEBIAN_FRONTEND noninteractive  
ADD bin/myinit.sh /bin/myinit.sh  
RUN chmod +x /bin/myinit.sh && \  
apt-get update && \  
apt-get install -y nginx-extras && \  
apt-get clean autoclean && apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
ADD etc/nginx/sites-available/default /etc/nginx/sites-available/default  
EXPOSE 80  
CMD /bin/myinit.sh  

