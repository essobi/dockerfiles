# This image is based on "debian:jessie"  
FROM postgres:9.6  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
git \  
lzop \  
python3 \  
python3-pip \  
python3-setuptools \  
pv \  
&& rm -rf /var/lib/apt/lists/*  
  
# Use pip3.4 to avoid conflict with system pip3  
RUN pip3 install -U pip \  
&& pip3.4 install --no-cache-dir
"git+https://github.com/pjknkda/wal-e.git@v1.1.1b3#egg=wal-e[azure]"

