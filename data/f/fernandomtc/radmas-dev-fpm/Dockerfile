FROM fernandomtc/radmas-iyc-common  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
php5-fpm \  
php5-redis \  
php5-xdebug  
  
RUN \  
rm -rf /var/lib/apt/lists/*  
  
CMD /bin/bash  

