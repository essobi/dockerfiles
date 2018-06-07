FROM vicgonco/apache2  
  
MAINTAINER Víctor González <victor.gonzalez@geomati.co>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://httpredir.debian.org/debian jessie contrib" >>
/etc/apt/sources.list  
RUN set -x \  
&& apt-get update \  
&& apt-get install -yq libapache2-modsecurity modsecurity-crs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mv /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf \  
&& sed -i 's#SecRuleEngine DetectionOnly#SecRuleEngine On#'
/etc/modsecurity/modsecurity.conf \  
&& sed -i 's#SecResponseBodyAccess On#SecResponseBodyAccess Off#'
/etc/modsecurity/modsecurity.conf \  
&& sed -i 's#SecRequestBodyLimit .*#SecRequestBodyLimit 52428800#'
/etc/modsecurity/modsecurity.conf \  
&& sed -i 's#</IfModule>#\tInclude "/usr/share/modsecurity-
crs/*.conf"\n</IfModule>#' /etc/apache2/mods-enabled/security2.conf \  
&& sed -i 's#</IfModule>#\tInclude "/usr/share/modsecurity-
crs/activated_rules/*.conf"\n</IfModule>#' /etc/apache2/mods-
enabled/security2.conf  
  
RUN ln -s /usr/share/modsecurity-crs/base_rules/* /usr/share/modsecurity-
crs/activated_rules/  
  
RUN a2enmod proxy_http rewrite  

