FROM httpd:2.4  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
nano \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /usr/local/apache2/conf \  
&& rm -rf /usr/local/apache2/htdocs  
  
COPY ./apache2 /usr/local/apache2  
  
EXPOSE 1080  
#COPY ./bin /usr/local/bin  
#CMD [ "custom-httpd-foreground" ]  

