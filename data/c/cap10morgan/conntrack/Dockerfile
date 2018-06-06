FROM cap10morgan/busybase:latest  
MAINTAINER Wes Morgan <cap10morgan@gmail.com>  
  
RUN opkg-install --nodeps conntrack-tools libnetfilter-conntrack libnfnetlink
libmnl  
  
ENTRYPOINT ["conntrack"]  
CMD []  

