FROM python:slim  
  
RUN apt-get update && \  
apt-get install git curl --no-install-recommends -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& curl -sSLo /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -sSLo /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Create unprivileged user  
RUN groupadd -r python && useradd -m -r -g python python  
  
# Add cookiecutter  
RUN pip install --no-cache-dir -U pip && \  
pip install --no-cache-dir cookiecutter  
  
COPY *.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

