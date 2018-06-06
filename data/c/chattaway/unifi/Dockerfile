FROM debian:stable-slim  
  
RUN mkdir --parents /usr/share/man/man1  
RUN echo 'deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti' >
/etc/apt/sources.list.d/100-ubnt-unifi.list  
RUN apt-get update && apt-get install -y --allow-unauthenticated unifi  
  
CMD ["/usr/bin/java", "-jar", "/usr/lib/unifi/lib/ace.jar", "start"]  
  
EXPOSE 8080 8443 8880 8843 6789 3478/udp  
  
VOLUME ["/usr/lib/unifi/data"]  

