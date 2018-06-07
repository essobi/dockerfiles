FROM ubuntu:14.04  
MAINTAINER Alexey Nurgaliev <atnurgaliev@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y python python-pip python-ldap mercurial git \  
python-dev software-properties-common libmysqlclient-dev libpq-dev \  
libffi-dev && \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
\  
mkdir /kallithea && \  
cd /kallithea && \  
mkdir -m 0777 config repos logs && \  
hg clone https://bitbucket.org/domruf/kallithea -u
af00d72ec329ddb807ef2f2f63c6f4a49432215b && \  
cd kallithea && \  
rm -r .hg && \  
pip install --upgrade pip setuptools && \  
pip install -e . && \  
python setup.py compile_catalog && \  
\  
pip install mysql-python && \  
pip install psycopg2 && \  
pip install hg-evolve && \  
\  
apt-get purge --auto-remove -y python-dev software-properties-common && \  
\  
rm /etc/nginx/sites-enabled/*  
  
RUN apt-get install -y wget  
  
#RUN cd /kallithea/kallithea; \  
# wget
https://bitbucket.org/kiilerix/kallithea/commits/a7b5cd25f5db028163d447077bfc47e318cbe2ec/raw/
-q -O - | patch -p1 -N; \  
# wget
https://bitbucket.org/kiilerix/kallithea/commits/5ec4d56faaf8240d5a7e4f6bf0055c78c4fb0250/raw/
-q -O - | patch -p1 -N; \  
# wget
https://bitbucket.org/kiilerix/kallithea/commits/7bb325660edc97fbd10ef63f4e57325153063684/raw/
-q -O - | patch -p1 -N; \  
# wget
https://bitbucket.org/kiilerix/kallithea/commits/a02455783d7824ec8479a260f9dbcb9f5a6c2209/raw/
-q -O - | patch -p1 -N  
ADD kallithea_vhost /etc/nginx/sites-enabled/kallithea_vhost  
ADD run.sh /kallithea/run.sh  
  
VOLUME ["/kallithea/config", "/kallithea/repos", "/kallithea/logs"]  
  
EXPOSE 80  
CMD ["/kallithea/run.sh"]  

