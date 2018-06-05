FROM progrium/busybox  
MAINTAINER Fletcher Nichol <fnichol@nichol.ca>  
  
RUN opkg-install uhttpd  
  
VOLUME ["/www"]  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/uhttpd", "-f", "-p", "80", "-h", "/www"]  
CMD [""]  

