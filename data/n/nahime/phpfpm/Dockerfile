FROM nahime/dotdeb  
MAINTAINER Vincenzo Petrucci (nahime)  
ENV DEBIAN_FRONTEND noninteractive  
ADD bin/myinit.sh /bin/myinit.sh  
RUN chmod +x /bin/myinit.sh && \  
apt-get update && \  
apt-get install -y php5-fpm && \  
apt-get clean autoclean && apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
EXPOSE 9000  
CMD /bin/myinit.sh  

