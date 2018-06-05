FROM phenompeople/centos-python:2.7.5  
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com" \  
project="elastalert"  
ADD requirements.txt /  
RUN pip install -q -r requirements.txt && \  
mkdir -p /opt/elastalert/{conf,bin} /var/log/elastalert && \  
touch /var/log/elastalert/elastalert.log && \  
ln -sf /opt/elastalert/conf /etc/elastalert && \  
rm -rf /requirements.txt  
ADD setup/config.yml /opt/elastalert/conf/config.yml  
ADD scripts /opt/elastalert/bin/  
VOLUME /etc/elastalert/conf.d  
ENTRYPOINT ["/opt/elastalert/bin/elastalert.sh"]  

