FROM python:2.7  
MAINTAINER Genadi Postrilko <genadipost@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
rsync \  
inkscape \  
apache2 \  
&& pip install giza \  
&& cd / \  
&& git clone https://github.com/mongodb/docs.git \  
&& cd /docs \  
&& make html \  
&& rm -rf /var/www/html \  
&& ln -s /docs/build/master/html/ /var/www/html  
  
EXPOSE 80  
CMD rm -f /usr/local/apache2/logs/httpd.pid && apachectl -DFOREGROUND  

