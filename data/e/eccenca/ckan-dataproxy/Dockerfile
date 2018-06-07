FROM eccenca/baseimage:1.0.1  
MAINTAINER Henri Knochenhauer <henri.knochenhauer@eccenca.com>  
MAINTAINER René Pietzsch <rene.pietzsch@eccenca.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN \  
apt-get update \  
&& apt-get install -y -qq --no-install-recommends \  
wget unzip python openssh-client python-openssl \  
&& apt-get clean \  
&& mkdir -p /var/log/dataproxy  
  
ADD dataproxy /data  
  
EXPOSE 8000  
WORKDIR /data  
  
CMD python /data/dataproxy/app.py 2>&1 | tee -a
/var/log/dataproxy/dataproxy.log  

