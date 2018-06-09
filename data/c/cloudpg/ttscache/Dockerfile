FROM cloudpg/centos-7-grid  
LABEL maintainer="mirco.tracolli@pg.infn.it"  
LABEL Version=1.0.1  
  
# GET_PROXY STUFF  
RUN yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install python python-pip \  
&& yum clean all \  
&& pip install --upgrade pip setuptools \  
&& pip install requests kazoo flask \  
&& mkdir -p /opt/ttscache/ \  
&& mkdir -p /var/log/ttscache/ \  
&& touch /var/log/ttscache/app.log  
COPY ./proxy_config.json ./proxy.py ./cache.py ./app_ttscache.py
/opt/ttscache/  
  
EXPOSE 80  
CMD ["/usr/bin/python", "/opt/ttscache/app_ttscache.py"]  
  
# Proxy config ENV variables: default or example values  
#  
# IAM_TOKEN: None  
# IAM_REFRESH_TOKEN: None  
# IAM_CLIENT_ID: None  
# IAM_CLIENT_SECRET: None  
# MARATHON_USER: None  
# MARATHON_PASSWD: None  
# ZOOKEEPER_HOST_LIST: None  
# CACHE_MANAGER: False  
# PROXY_AUDIENCE: "https://example.url.org",  
# PROXY_TTS: "https://example.url.org",  
# PROXY_IAM_ENDPOINT: "https://example.endpoint/",  
# PROXY_CREDENTIAL_ENDPOINT: "https://example.url.org/api/v2/iam/credential",  
# PROXY_LOCAL_CACHE_EXPIRATION_TIME: 864000,  
# PROXY_LOCK_FILE_AGE: 20,  
# PROXY_CACHE_DIR: "/tmp"  

