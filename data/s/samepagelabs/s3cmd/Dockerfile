FROM debian:jessie  
  
ENV S3_TOOLS_VERSION 1.6.1  
RUN \  
apt-get -y update && \  
apt-get --no-install-recommends --assume-yes install python-setuptools python-
magic ca-certificates wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
wget
"http://downloads.sourceforge.net/project/s3tools/s3cmd/${S3_TOOLS_VERSION}/s3cmd-${S3_TOOLS_VERSION}.tar.gz"
-q -O - | tar xz -C /tmp && \  
cd /tmp/s3cmd-${S3_TOOLS_VERSION} && \  
python setup.py install && \  
cd / && \  
rm -rf /tmp/s3cmd  
  
ENTRYPOINT ["/usr/local/bin/s3cmd"]  

