FROM solsson/svn-httpd:1.9  
RUN sed -i 's|^#LoadModule authn_anon_module|LoadModule authn_anon_module|'
conf/httpd.conf  
  
RUN echo "Include conf/proxied/*.conf" >> conf/httpd.conf  
  
COPY proxied/* conf/proxied/  

