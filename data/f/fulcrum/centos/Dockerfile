FROM docker.io/centos:centos7  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
# Upgrade and cleanup packages  
RUN echo "Cache bust 201604291406" && \  
yum --noplugins upgrade -y && \  
yum --noplugins install -y yum-utils && \  
package-cleanup --dupes && \  
package-cleanup --cleandupes && \  
yum clean all  

