FROM voobscout/base-arch  
MAINTAINER Voobscout <voobscout@archlinux.info>  
  
ENV container docker  
ENV TERM screen  
  
COPY update-repo /usr/local/bin/update-repo  
RUN /usr/local/bin/update-repo  
  
COPY pkg-init /usr/local/bin/pkg-init  
CMD ["/usr/local/bin/pkg-init"]  

