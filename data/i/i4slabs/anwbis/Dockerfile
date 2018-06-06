FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -qyy \  
-o APT::Install-Recommends=false -o APT::Install-Suggests=false \  
python python-dev python-pip git python-setuptools \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /root/.cache \  
&& pip install -U awscli requests \  
&& git clone https://github.com/i4slabs/anwbis.git \  
&& cd anwbis \  
&& python setup.py install \  
&& cd / \  
&& rm -rf /anwbis \  
&& adduser --home /var/jenkins_home --shell /bin/bash --uid 1000 --ingroup
nogroup --disabled-password -q anwbis  
  
USER anwbis  
  
ENTRYPOINT ["anwbis"]  
  
CMD ["--help"]  

