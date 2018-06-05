FROM alpine  
MAINTAINER John McCabe <john@johnmccabe.net>  
  
# Expose ports  
EXPOSE 8123  
  
RUN mkdir -p /etc/polipo \  
&& mkdir /cache  
ADD assets/polipo /usr/bin/polipo  
ADD assets/config /etc/polipo/config  
  
# Expose the cache directory  
VOLUME ["/cache"]  
  
ENTRYPOINT [ "/usr/bin/polipo", "-c", "/etc/polipo/config" ]  

