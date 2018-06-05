FROM fedora:latest  
# bird  
MAINTAINER Matthew McKenzie <matthew.mckenzie@rungeict.com>  
COPY resources/ /  
RUN dnf -y install bird  
VOLUME ["/var/log", "/var/run", "/etc/bird.d"]  
EXPOSE 179/tcp  
ENTRYPOINT ["/usr/sbin/bird"]  
CMD ["-c", "/etc/bird.conf", "-s", "/var/run/bird.ctl", "-f"]

