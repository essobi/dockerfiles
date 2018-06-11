FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
LABEL io.k8s.description="Fluentd for Kubernetes" \  
io.k8s.display-name="Fluentd for Kubernetes"  
  
ADD files/etc/yum.repos.d /etc/yum.repos.d  
RUN rpm -ivh
https://packages.graylog2.org/repo/packages/graylog-2.0-repository_latest.rpm
&& \  
yum install -y td-agent bind-utils gcc-c++ libcurl-devel make && \  
yum clean all -y && \  
/usr/sbin/td-agent-gem install fluent-plugin-kubernetes_metadata_filter
fluent-plugin-flatten-hash fluent-plugin-burrow gelf  
  
ADD files /  
RUN chmod 755 /usr/bin/run-fluentd  
  
ENV GRAYLOG_LOG_LEVEL=info  
  
USER 0  
VOLUME /var/log  
VOLUME /var/lib/docker/containers  
CMD ["run-fluentd"]  

