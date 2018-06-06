FROM debian:jessie  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
CMD []  
ENTRYPOINT ["/usr/bin/turnserver", "-n", "--log-file", "stdout"]  
EXPOSE 3478 3478/udp  
  
# Workaround for https://github.com/docker/docker/issues/6345  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends coturn curl procps  

