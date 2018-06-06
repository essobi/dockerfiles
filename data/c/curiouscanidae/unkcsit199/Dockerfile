#Gets a base image, in this case Debian.  
FROM debian:latest  
  
#Specify environment variable  
ENV S6_RELEASE 1.21.4.0  
#Installs S6 Overlay.  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_RELEASE/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
#Installs useless programs  
RUN apt-get update  
RUN apt-get install cowsay fortune -y  
  
#Copy Install script into the Container to be executed on startup.  
COPY install.sh /etc/cont-init.d/  
  
#Anything in the init.d will automatically run.  
RUN chmod u+x /etc/cont-init.d/install.sh  
  
ENTRYPOINT ["/init"]  

