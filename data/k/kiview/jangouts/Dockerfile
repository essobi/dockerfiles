FROM httpd:2.4.25  
RUN apt-get update && apt-get install -y wget  
  
ENV DOCKERIZE_VERSION v0.4.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
ENV JANGOUTS_VERSION v0.4.5  
RUN wget https://github.com/jangouts/jangouts/archive/$JANGOUTS_VERSION.tar.gz
\  
&& mkdir /jangouts \  
&& tar -C /jangouts -xzvf $JANGOUTS_VERSION.tar.gz --strip 1 \  
&& cp -a /jangouts/dist/. /usr/local/apache2/htdocs/ \  
&& rm -R /jangouts \  
&& rm $JANGOUTS_VERSION.tar.gz  
  
COPY config.tmpl.json /usr/local/apache2/htdocs/config.tmpl.json  
  
ENV JANUS_SERVER janus  
  
CMD ["dockerize", "-template",
"/usr/local/apache2/htdocs/config.tmpl.json:/usr/local/apache2/htdocs/config.json",
"httpd-foreground"]

