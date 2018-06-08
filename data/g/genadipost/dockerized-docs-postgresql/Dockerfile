FROM httpd:latest  
MAINTAINER Genadi Postrilko <genadipost@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
ca-certificates \  
tar \  
&& cd / \  
&& curl https://ftp.postgresql.org/pub/source/v9.6.1/postgresql-9.6.1.tar.gz
-o postgresql-9.6.1.tar.gz \  
&& tar -xvf postgresql-9.6.1.tar.gz -C . \  
&& rm -rf /usr/local/apache2/htdocs \  
&& ln -s /postgresql-9.6.1/doc/src/sgml/html /usr/local/apache2/htdocs  

