FROM debian:jessie  
MAINTAINER "Herlon Aguiar" <herlon214@gmail.com>  
  
COPY src/* /tmp/  
RUN /bin/bash /tmp/docker-install.sh \  
&& rm -rvf /tmp/*  
  
EXPOSE 6081  
EXPOSE 6085  
ENTRYPOINT ["/usr/local/bin/chaperone"]  
CMD ["--user", "varnish"]  

