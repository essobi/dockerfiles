FROM centos:latest  
MAINTAINER dayreiner  
  
ENV HAPROXY_MAJOR 1.6  
ENV HAPROXY_VERSION 1.6.5  
ENV HAPROXY_MD5 5290f278c04e682e42ab71fed26fc082  
  
RUN yum -y update && yum clean all \  
&& yum -y install which  
  
COPY scripts/docker-entrypoint.sh /  
  
RUN buildDeps="gcc make pcre-static pcre-devel openssl-devel zlib-devel" \  
&& yum -y install ${buildDeps} \  
&& curl -SL
"http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz"
-o haproxy.tar.gz \  
&& echo "${HAPROXY_MD5} haproxy.tar.gz" | md5sum -c \  
&& mkdir -p /usr/src/haproxy \  
&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \  
&& rm haproxy.tar.gz \  
&& make -C /usr/src/haproxy \  
TARGET=linux2628 \  
USE_PCRE=1 PCREDIR= \  
USE_OPENSSL=1 \  
USE_ZLIB=1 \  
all \  
install-bin \  
&& mkdir -p /usr/local/etc/haproxy \  
&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \  
&& rm -rf /usr/src/haproxy \  
&& yum -y remove ${buildDeps}  
  
RUN useradd -r haproxy \  
&& chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]  

