FROM elcom/drupal  
MAINTAINER LWB  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-
recommends \  
openjdk-8-jre libreoffice-writer && \  
mkdir -p /var/www/.config/libreoffice/4/user && \  
rm -rf /var/lib/apt/lists  
  
COPY registrymodifications.xcu /var/www/.config/libreoffice/4/user/  
  
RUN chmod o+r /var/www/.config/libreoffice/4/user/registrymodifications.xcu  

