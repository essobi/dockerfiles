FROM ubuntu:xenial  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -qyy \  
-o APT::Install-Recommends=false -o APT::Install-Suggests=false \  
python-pip python-setuptools \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install awscli  
  
RUN adduser --home /var/jenkins_home --shell /bin/bash --uid 1000 --ingroup
nogroup --disabled-password -q awscli  
  
USER awscli  
  
ENTRYPOINT ["/usr/local/bin/aws"]  
  
CMD ["--help"]  

