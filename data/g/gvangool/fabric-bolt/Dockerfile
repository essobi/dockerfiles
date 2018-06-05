FROM centos:7  
MAINTAINER Gert Van Gool <gert@vangool.mx>  
  
RUN yum install -y epel-release && \  
yum update -y && \  
yum clean all  
  
RUN yum install -y python{,-devel} gcc libxml2{,-devel} libxslt{,-devel} git
&& \  
yum clean all && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm -f get-pip.py  
  
ENV PIP_NO_CACHE_DIR "off"  
ENV REPO https://github.com/fabric-bolt/fabric-bolt.git  
ENV VERSION 9d046dcea8bac7c3f4b813d77c647ae14e63bbe6  
  
RUN mkdir -p /src && \  
git clone ${REPO} /src/fabric-bolt && \  
cd /src/fabric-bolt && \  
git checkout ${VERSION} && \  
pip install -e . && \  
pip install uwsgi  
  
ENV FABRIC_BOLT_CONF /root/.fabric-bolt/settings.py  
  
RUN touch /src/run && \  
chmod +x /src/run && \  
echo '#!/bin/bash' >> /src/run && \  
echo 'test -f "${FABRIC_BOLT_CONF}" || fabric-bolt init' >> src/run && \  
echo 'fabric-bolt migrate --noinput' >> /src/run && \  
echo 'fabric-bolt collectstatic --noinput' >> /src/run && \  
echo 'uwsgi --http=:8000 --chdir=/src/fabric-bolt/ --wsgi-
file=fabric_bolt/wsgi.py --master --processes=4 --threads=2
--stats=0.0.0.0:9000 --check-static /src/fabric-bolt/fabric_bolt/core/public'
>> /src/run && \  
echo '' >> /src/run  
  
EXPOSE 8000 9000  
CMD ["/src/run"]  

