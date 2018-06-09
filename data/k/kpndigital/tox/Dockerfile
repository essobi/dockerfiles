FROM ubuntu:17.04  
ENV python2Versions='python2.7'  
ENV python3Versions='python3.5 python3.6'  
ENV pythonVersions="$python2Versions $python3Versions"  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $pythonVersions \  
&& apt-get install -y $(for pyver in $pythonVersions; do echo $pyver-dev;
done) \  
&& apt-get install -y $(for py3ver in $python3Versions; do echo $py3ver-venv;
done) \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install time netcat gettext libjpeg-dev curl git-core build-
essential \  
make build-essential libssl-dev zlib1g-dev libbz2-dev \  
libreadline-dev libsqlite3-dev -y \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY get-pip.py /tmp/get-pip.py  
  
RUN for pybin in $pythonVersions; do $pybin /tmp/get-pip.py; done && rm -rf
/tmp/get-pip.py  
  
RUN apt-get update \  
&& apt-get install -y virtualenv \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ln -s `which python2.7` /usr/bin/python2  
RUN ln -s `which virtualenv` /usr/local/bin/virtualenv-2.7  
  
RUN apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
ca-certificates \  
software-properties-common \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \  
&& apt-get update \  
&& apt-get install -y docker-ce \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker-compose /usr/local/bin/docker-compose  

