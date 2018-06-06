FROM php:5-apache  
  
# Packages  
RUN apt-get update && \  
apt-get install wget cron git -y  
  
# Install s6-overlay  
# (https://github.com/just-containers/s6-overlay)  
ENV S6_OVERLAY_VER 1.19.1.1  
RUN wget -qO- https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VER}/s6-overlay-
amd64.tar.gz | tar xz -C /  
  
# Install cheky  
# (https://github.com/Blount/LBCAlerte/)  
WORKDIR /tmp  
RUN git clone https://github.com/Blount/LBCAlerte.git -b dev  
  
RUN rm -fr /var/www/html && \  
mv /tmp/LBCAlerte /var/www/html  
RUN chown -R www-data:www-data /var/www/html  
  
# Copy all the rootfs dir into the container  
COPY rootfs /  
  
# Set s6-overlay as entrypoint  
ENTRYPOINT ["/init"]  

