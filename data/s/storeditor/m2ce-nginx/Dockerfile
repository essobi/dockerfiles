FROM nginx:1.12  
#Copy configuration and operation files  
COPY . /tmp/  
  
RUN rm -f /etc/nginx/conf.d/* && \  
mv /tmp/bin/* /usr/local/bin/ && \  
mv /tmp/conf/nginx.conf /etc/nginx/ && \  
mv /tmp/conf/conf.d/mage.conf /etc/nginx/conf.d/ && \  
apt-get update && apt-get install -y cron \  
python-openssl \  
python-crypto \  
python-setuptools \  
python-pip && \  
pip install acme-nginx && \  
apt-get clean  
  
WORKDIR /srv/www  
  
CMD ["/usr/local/bin/start.sh"]  

