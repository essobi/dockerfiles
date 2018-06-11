FROM ubuntu:latest  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y install unbound  
EXPOSE 53/udp 53/tcp  
CMD ["unbound"]  
# COPY tcp.conf /etc/unbound/unbound.conf.d/

