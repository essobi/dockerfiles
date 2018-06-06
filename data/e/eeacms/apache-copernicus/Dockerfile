FROM eeacms/apache:2.4s  
COPY mod* /usr/local/apache2/modules  
RUN chown -R apache:apache /usr/local/apache2/modules/ \  
&& echo "LoadModule proxy_html_module modules/mod_proxy_html.so" >>
conf/httpd.conf \  
&& apt-get update \  
&& apt-get install --no-install-recommends libxml2 \  
&& rm -rf /var/lib/apt/lists/*  

