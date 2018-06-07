FROM buildpack-deps:xenial-scm  
MAINTAINER Presslabs <ping@presslabs.com>  
  
ENV DEBUILD_OPTS="-us -uc -b"  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y devscripts debhelper build-essential equivs software-
properties-common quilt dh-autoreconf uuid-dev \  
&& mkdir -p /target /source /secrets  
WORKDIR /source  
VOLUME ["/target", "/source", "/secrets"]  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["make", "binary"]  

