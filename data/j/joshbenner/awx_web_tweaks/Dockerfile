FROM ansible/awx_web:1.0.1.31  
ENV ANSIBLE_VERSION=2.4.1.0-0.3.rc1  
  
USER root  
  
RUN sed -i 's/localhost/127.0.0.1/g' /etc/nginx/nginx.conf && \  
pip install netaddr jmespath && \  
cd /var/lib/awx && \  
curl -L -O
https://github.com/ansible/ansible/archive/v${ANSIBLE_VERSION}.tar.gz && \  
tar -xzvf v${ANSIBLE_VERSION}.tar.gz && \  
cd ansible-${ANSIBLE_VERSION} && \  
python setup.py install && \  
cd .. && rm -rf ansible-${ANSIBLE_VERSION} v${ANSIBLE_VERSION}.tar.gz  
  
USER 1000  

