FROM centos:centos7  
  
LABEL maintainer="Jamie Isaacs <pdt256@gmail.com>"  
  
WORKDIR /usr/local/src  
  
ENV SPHINX_VERSION=2.2.11-1  
ENV
SPHINX_URL="http://sphinxsearch.com/files/sphinx-$SPHINX_VERSION.rhel7.x86_64.rpm"
\  
BUILD_DEPENDENCIES="wget"  
RUN yum -y update \  
&& yum -y install \  
postgresql-libs \  
unixODBC \  
mysql \  
$BUILD_DEPENDENCIES \  
&& wget -q $SPHINX_URL -O sphinx.rpm \  
&& yum -y install sphinx.rpm \  
&& rm sphinx.rpm \  
&& yum -y remove $BUILD_DEPENDENCIES \  
&& yum clean all \  
\  
&& mkdir -p /var/lib/sphinx/data \  
&& mkdir -p /var/log/sphinx \  
&& mkdir -p /var/run/sphinx  
  
COPY ./wait-for-mysql.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/wait-for-mysql.sh  
  
EXPOSE 9306  
CMD ["searchd", "--nodetach"]  

