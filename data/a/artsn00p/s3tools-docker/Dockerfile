FROM fedora:latest  
  
MAINTAINER Artem Silenkov <artem.silenkov@gmail.com>  
  
ENV S3_TOOLS_VERSION 2.0.1  
RUN \  
dnf -y update && \  
dnf install -y python-setuptools python-magic ca-certificates wget && \  
dnf clean all  
  
RUN \  
wget
"http://downloads.sourceforge.net/project/s3tools/s3cmd/${S3_TOOLS_VERSION}/s3cmd-${S3_TOOLS_VERSION}.tar.gz"
-q -O - | tar xz -C /tmp && \  
cd /tmp/s3cmd-${S3_TOOLS_VERSION} && \  
python setup.py install && \  
cd / && \  
rm -rf /tmp/s3cmd  
  
ENTRYPOINT ["/usr/local/bin/s3cmd"]  

