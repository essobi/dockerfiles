FROM httpd:2.4  
RUN apt-get update  
  
RUN apt-get -y install \  
wget \  
net-tools  
  
COPY . /usr/local/apache2/htdocs/  
COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf  
COPY . /var/lib/apache  
EXPOSE 8080  

