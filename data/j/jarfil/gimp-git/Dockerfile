FROM debian:testing  
MAINTAINER Jaroslaw Filiochowski <jarfil@gmail.com>  
  
# compile  
ADD make_gimp.sh /root/make_gimp.sh  
RUN chmod +x /root/make_gimp.sh  
RUN ["/bin/bash", "-c", "/root/make_gimp.sh"]  
  
# entry point  
WORKDIR /  
ENTRYPOINT /usr/local/bin/gimp  

