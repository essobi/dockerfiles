FROM kalilinux/kali-linux-docker  
MAINTAINER Christopher Warmbold (warch)  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
libapache2-mod-php5 \  
set \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
;rm -Rf /var/cache \  
;rm /tmp/* \  
;apt-get autoremove -y  
  
EXPOSE 80 3000  
  
CMD ["setoolkit"]

