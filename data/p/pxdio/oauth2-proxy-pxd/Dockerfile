FROM pxdio/oauth2-proxy  
ADD template-sources /tmp/template-sources/  
RUN mkdir -p /var/lib/oauth2_proxy/templates/  
RUN cat /tmp/template-sources/header.html /tmp/template-sources/error.html
/tmp/template-sources/footer.html > /var/lib/oauth2_proxy/templates/error.html  
RUN cat /tmp/template-sources/header.html /tmp/template-sources/sign_in.html
/tmp/template-sources/footer.html >
/var/lib/oauth2_proxy/templates/sign_in.html  
RUN rm -r /tmp/*  

