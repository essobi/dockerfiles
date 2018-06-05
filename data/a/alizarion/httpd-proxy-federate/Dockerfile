FROM alizarion/httpd:latest  
  
ADD mod_openid_conf.template /tmp/  
ADD shibboleth2_xml.template /tmp/  
ADD entrypoint.sh /  
ADD start.sh /  
RUN chmod +x /start.sh  
RUN chmod +x /entrypoint.sh  
  
RUN rm -f /usr/share/httpd/noindex/index.html  
ADD index.html /usr/share/httpd/noindex/  
RUN chmod 777 /usr/share/httpd/noindex/index.html  
  
RUN curl -o /etc/yum.repos.d/security:shibboleth.repo
http://download.opensuse.org/repositories/security://shibboleth/CentOS_7/security:shibboleth.repo  
  
RUN yum -y swap -- remove systemd-container systemd-container-libs -- install
systemd systemd-libs  
RUN yum -y install shibboleth  
  
ADD mod_shib_saml.conf /etc/httpd/conf.d/  
  
ADD sp-key.pem /etc/shibboleth/  
ADD sp-cert.pem /etc/shibboleth/  
RUN rm -f /etc/httpd/conf.d/shib.conf  
RUN rm -f /etc/shibboleth/shibboleth2.xml  
RUN rm -f /etc/shibboleth/attribute-map.xml  
ADD attribute-map.xml /etc/shibboleth/  
ADD keycloakmetadata.xml /etc/shibboleth/  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD sh /start.sh  

