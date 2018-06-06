FROM debian:sid  
  
RUN apt-get update -q && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y freeipa-server && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN a2enmod proxy_ajp && \  
sed -ri ' \  
s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \  
s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \  
' /etc/apache2/conf-available/* /etc/apache2/sites-available/*  
  
RUN sed -i 's|sha|SHA|g;' /usr/lib/python2.7/dist-
packages/ipalib/plugins/otptoken.py /usr/share/ipa/ui/js/freeipa/app.js && \  
rm /usr/lib/python2.7/dist-packages/ipalib/plugins/otptoken.pyc && \  
python -m compileall /usr/lib/python2.7/dist-
packages/ipalib/plugins/otptoken.py  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

