FROM radmas/mtc-plus-fpm  
  
MAINTAINER Fernando Moro <fernando.moro@radmas.com>  
  
LABEL org.mejoratuciudad.vendor="Radmas Technologies"  
LABEL org.mejoratuciudad.image-name="mtc-plus-application"  
LABEL description="Symfony2 Backoffice for Improve Your City."  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# NGINX  
  
# Install PPA dependencies  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
software-properties-common  
  
# Add nginx PPA  
RUN \  
apt-add-repository -y ppa:nginx/stable  
  
# Update apt cache with PPA  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
nginx-full && \  
rm -rf /var/lib/apt/lists/*  
  
# Remove unused dependencies  
RUN \  
apt-get remove --purge -y \  
software-properties-common &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/var/cache/nginx"]  
  
#################################################  
# S6 OVERLAY  
  
USER root  
  
ENTRYPOINT ["/init"]  

