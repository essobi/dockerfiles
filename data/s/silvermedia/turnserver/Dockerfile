FROM centos:7.4.1708  
# Application settings  
ENV TURNSERVER_VERSION="4.5.0.7" \  
CONTAINER_NAME="turnserver"  
# Install extra package  
RUN yum install -y curl tar bash wget sudo && \  
curl -s -S
http://coturn.net/turnserver/v${TURNSERVER_VERSION}/turnserver-${TURNSERVER_VERSION}-CentOS7.4-x86_64.tar.gz
-o /tmp/turnserver-${TURNSERVER_VERSION}-CentOS7.4-x86_64.tar.gz && \  
tar -xzf /tmp/turnserver-${TURNSERVER_VERSION}-CentOS7.4-x86_64.tar.gz -C /tmp
&& \  
cd /tmp/turnserver-${TURNSERVER_VERSION} && \  
./install.sh && \  
chmod -x /usr/lib/systemd/system/turnserver.service && \  
rm -rf /tmp/turnserver-${TURNSERVER_VERSION} && \  
yum clean all  
  
EXPOSE 3478 5349  
USER turnserver  
  
CMD ["/usr/bin/turnserver", "-c /etc/turnserver/turnserver.conf"]

