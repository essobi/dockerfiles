FROM chrisgarrett/athenapdf-service-base  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
msttcorefonts \  
ttf-mscorefonts-installer \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc /usr/share/doc-base /usr/share/man /usr/share/locale
/usr/share/zoneinfo /var/cache/debconf/*-old \  
&& rm -rf /var/lib/cache /var/lib/log \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  
  

