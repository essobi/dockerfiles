FROM jenkins  
MAINTAINER Rafael Pivato <rafael.pivato@seniorgrowth.com>  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y \  
git \  
libffi-dev \  
libjpeg-dev \  
libmemcached-dev \  
libpq-dev \  
postgresql-client \  
python \  
python-dev \  
python-pip \  
python-psycopg2 \  
ruby \  
zlib1g-dev \  
&& pip install --upgrade \  
pip \  
virtualenv \  
awscli \  
awsebcli \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
  
  
#USER jenkins # drop back to the regular jenkins user - good practice  

