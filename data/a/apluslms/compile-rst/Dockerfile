FROM debian:stretch-slim  
  
ENV LANG=C.UTF-8  
  
RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
--no-install-recommends \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
apt-utils \  
ca-certificates \  
make \  
python3 \  
python3-pip \  
python3-setuptools \  
python3-yaml \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& pip3 install --no-cache-dir --disable-pip-version-check \  
"sphinx<1.7" \  
Unidecode \  
&& rm -rf /root/.cache  
  
WORKDIR /compile  
VOLUME /compile  
  
CMD ["make"]  

