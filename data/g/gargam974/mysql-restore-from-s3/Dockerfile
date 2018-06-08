FROM mysql:5.6  
LABEL maintainer="gargam974@gmail.com"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-pip \  
curl \  
&& pip --no-cache-dir install setuptools \  
&& pip --no-cache-dir install awscli \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY import-s3.sh /docker-entrypoint-initdb.d/  

