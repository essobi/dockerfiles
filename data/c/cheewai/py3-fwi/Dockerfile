FROM cheewai/py3-psycopg2  
LABEL maintainer "Cheewai Lai <clai@csir.co.za?"  
  
ARG BRANCH=master  
ARG REPO=https://github.com/Terranex/pyfwi/archive/${BRANCH}.zip  
#  
# By default, setuptools installs pyFWI module to  
# /usr/local/lib/python3.6/site-packages  
# Force it to /usr/lib/python3.6/site-packages instead to avoid  
# having to modify PYTHONPATH  
#  
# astral - CAFWI zenith hour  
# raven - sentry.io logging  
# xmltodict - parse yr.no response  
#  
RUN apk update \  
&& apk add curl unzip py3-astral@testing py3-raven py3-requests
py3-xmltodict@testing py3-dateutil py3-urllib3 \  
&& pip install --upgrade pip \  
&& pip install python3-memcached \  
&& curl -o /tmp/pyfwi.zip -fsSL ${REPO} \  
&& cd /tmp \  
&& unzip pyfwi.zip \  
&& cd pyfwi-${BRANCH} \  
&& python setup.py install --prefix=/usr \  
&& rm -rf /var/cache/apk/*  

