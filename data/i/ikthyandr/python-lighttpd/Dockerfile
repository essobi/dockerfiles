FROM debian:jessie  
MAINTAINER Arnab Somadder <arnab.s@lowerentropy.com>  
  
RUN apt-get -y update\  
&& apt-get -y install python lighttpd\  
&& lighty-enable-mod cgi  
  
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf  
COPY 10-cgi.conf /etc/lighttpd/conf-available/10-cgi.conf  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/lighttpd"]  
CMD ["-f", "/etc/lighttpd/lighttpd.conf", "-D", "start"]  

