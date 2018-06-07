FROM ubuntu:16.04  
  
MAINTAINER Douglas Mueller <superbob@dthm.net>  
  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties && \  
apt-add-repository ppa:mumble/release && \  
apt-get update && \  
apt-get install -y mumble-server && \  
apt-get clean && rm -Rf /var/lib/apt/lists  
  
  
COPY src/entrypoint.sh /  
RUN chmod 755 /entrypoint.sh && mkdir -pv /mumble-server && chown -Rv mumble-
server:mumble-server /mumble-server  
VOLUME ["/mumble-server"]  
  
EXPOSE 64738 64738/udp  
ENTRYPOINT ["/entrypoint.sh"]  
USER mumble-server  
CMD ["/usr/sbin/murmurd", "-ini", "/mumble-server/mumble-server.ini", "-fg"]  

