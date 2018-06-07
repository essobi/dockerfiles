FROM kamaninga/bootstrap  
  
ENV DOCKER_CONF_HOME=/opt/docker/ \  
LOG_STDOUT="" \  
LOG_STDERR=""  
  
COPY conf/ /opt/docker/  
  
RUN /usr/local/bin/apk-install \  
python \  
python-dev \  
py-setuptools \  
py-crypto \  
py2-pip \  
py-cparser \  
py-cryptography \  
py-markupsafe \  
py-cffi \  
py-yaml \  
py-jinja2 \  
py-paramiko \  
&& pip install --upgrade pip \  
&& hash -r \  
&& pip install --no-cache-dir ansible \  
&& chmod 750 /usr/bin/ansible* \  
&& apk del python-dev \  
&& docker-image-cleanup  
  
RUN chmod +x /opt/docker/bin/* \  
&& /usr/local/bin/apk-install \  
supervisor \  
wget \  
curl \  
sed \  
gnupg \  
&& chmod +s /usr/local/bin/gosu \  
&& /opt/docker/bin/provision run --tag bootstrap --role webdevops-base \  
&& /opt/docker/bin/bootstrap.sh \  
&& docker-image-cleanup  
  
ENTRYPOINT ["/opt/docker/bin/entrypoint.sh"]  
CMD ["supervisord"]  

