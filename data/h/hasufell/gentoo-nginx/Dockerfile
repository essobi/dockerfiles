FROM hasufell/gentoo-amd64-paludis:latest  
MAINTAINER Julian Ospald <hasufell@gentoo.org>  
  
  
##### PACKAGE INSTALLATION #####  
# copy paludis config  
COPY ./config/paludis /etc/paludis  
  
# update world with our USE flags  
RUN chgrp paludisbuild /dev/tty && cave resolve -c world -x && \  
cave resolve -c tools -x && \  
cave resolve -c nginx -x && \  
etc-update --automode -5 && \  
rm -rf /usr/portage/distfiles/* /var/tmp/paludis/* \  
/var/tmp/portage/*  
  
################################  
# copy nginx config  
COPY ./config/nginx.conf /etc/nginx/nginx.conf  
COPY ./config/sites-enabled /etc/nginx/sites-enabled  
COPY ./config/sites-available /etc/nginx/sites-available  
  
# set up modescurity  
RUN cp /etc/nginx/modsecurity/modsecurity.conf \  
/etc/nginx/modsecurity/modsecurity.conf.orig  
RUN git clone \--depth=1 https://github.com/SpiderLabs/owasp-modsecurity-
crs.git \  
/etc/modsecurity  
RUN cat /etc/modsecurity/base_rules/*.conf >> \  
/etc/nginx/modsecurity/modsecurity.conf && \  
cp /etc/modsecurity/base_rules/*.data /etc/nginx/modsecurity/  
RUN sed -i \  
-e 's|SecRuleEngine .*$|SecRuleEngine On|' \  
/etc/nginx/modsecurity/modsecurity.conf  
COPY ./config/update-modsec.sh /usr/bin/update-modsec.sh  
RUN chmod +x /usr/bin/update-modsec.sh  
  
# supervisor config  
COPY ./config/supervisord.conf /etc/supervisord.conf  
  
# web server  
EXPOSE 80 443  
# create common group to be able to synchronize permissions to shared data
volumes  
RUN groupadd -g 777 www  
  
CMD exec /usr/bin/supervisord -n -c /etc/supervisord.conf  

