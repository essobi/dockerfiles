FROM kylejohnson/zoneminder:latest  
  
MAINTAINER MiGoller  
  
# Install PHP opcache und APCu support.  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y php7.0-opcache php-apcu  
  
# Add software-properties-common to enable adding additional repositories.  
RUN set -x \  
&& apt-get install -y software-properties-common  
  
# Must add DEBIAN repository to be able to install backward compatibility for
APCu.  
RUN set -x \  
&& add-apt-repository -y "deb http://ftp.de.debian.org/debian sid main" \  
&& apt-get update \  
&& apt-get install -y --allow-unauthenticated php-apcu-bc  
  
# Clean up  
RUN set -x \  
&& rm -rf /var/lib/apt/lists/*  
  
# Tweak the Docker command.  
CMD /ZoneMinder/utils/docker/setup.sh && /ZoneMinder/utils/docker/start.sh
>/var/log/start.log 2>&1  

