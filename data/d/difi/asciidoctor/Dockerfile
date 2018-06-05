FROM asciidoctor/docker-asciidoctor:latest  
  
ENV diagram false  
ENV epub false  
ENV pdf false  
  
ADD files /source  
RUN chmod a+x /source/*.sh \  
&& ln -s /source/saxon-xslt.sh /usr/bin/saxon-xslt \  
&& ln -s /source/saxon-xquery.sh /usr/bin/saxon-xquery \  
&& wget -nv http://central.maven.org/maven2/net/sf/saxon/Saxon-
HE/9.7.0-18/Saxon-HE-9.7.0-18.jar -O /source/saxon.jar  
  
VOLUME /target  
  
CMD ["sh", "/source/run.sh"]  

