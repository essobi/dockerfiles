# Gets a base image, in this case Debian  
FROM debian:latest  
  
# Environment variables for this Dockerfile  
ENV S6_RELEASE 1.21.4.0  
# Installs S6 Overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_RELEASE/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
# Installs a few useless applications  
RUN apt-get update \  
&& apt-get install cowsay fortune -y  
  
# Copy the install script into the Container to be executed on startup  
COPY install.sh /etc/cont-init.d/  
RUN chmod u+x /etc/cont-init.d/install.sh  
  
ENTRYPOINT ["/init"]  

