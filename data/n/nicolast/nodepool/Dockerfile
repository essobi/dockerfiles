FROM docker.io/centos:7.4.1708  
ARG version=3.0.1  
# Install runtime dependencies  
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \  
yum install -y \  
python35u \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum  
  
VOLUME /etc/nodepool  
  
RUN adduser --system nodepool --home-dir /var/lib/nodepool --create-home  
  
# Install build-time dependencies, package and remove build-time dependencies  
RUN yum install -y \  
python35u-pip \  
&& \  
pip3.5 install nodepool==$version && \  
rm -rf ~/.cache/pip && \  
yum remove -y \  
python35u-pip \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum  
  
USER nodepool:nodepool  
ENTRYPOINT ["nodepool-launcher", "-d", "-c", "/etc/nodepool/nodepool.yaml"]  

