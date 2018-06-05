FROM debian:7.6  
MAINTAINER pihizi@msn.com  
  
RUN apt-get -q update && apt-get install -y --force-yes --no-install-
recommends --auto-remove aria2 && rm -rf /var/lib/apt/lists/*  
  
# aria2.conf  
ADD aria2.conf /etc/aria2/aria2.conf  
  
# aria2 downloaded callback  
ADD download-complete.sh /etc/conf/aria2/download-complete.sh  
  
EXPOSE 6800  
# CMD ["/usr/bin/aria2c", "--conf-path=/etc/aria2/aria2.conf", "-D"]  
CMD ["/usr/bin/aria2c", "--conf-path=/etc/aria2/aria2.conf"]  

