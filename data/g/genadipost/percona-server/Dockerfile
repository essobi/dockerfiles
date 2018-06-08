FROM httpd:2.4.25-alpine  
MAINTAINER Genadi Postrilko <genadipost@gmail.com>  
  
RUN apk add --no-cache \  
\--update \  
make \  
python \  
py-pip \  
git \  
openssl \  
&& pip install sphinx \  
&& cd / \  
&& git clone https://github.com/percona/percona-server \  
&& cd /percona-server/doc \  
&& make html \  
&& rm -rf /usr/local/apache2/htdocs \  
&& ln -s /percona-server/doc/build/html /usr/local/apache2/htdocs  

