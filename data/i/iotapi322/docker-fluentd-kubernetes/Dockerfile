  
FROM centos:7  
RUN yum update -y && \  
yum install -y centos-release-scl-rh && \  
yum install -y scl-utils make gcc bzip2 rh-ruby23 rh-ruby23-ruby-devel && \  
yum clean all  
  
ENV LD_LIBRARY_PATH /opt/rh/rh-ruby23/root/usr/lib64  
ENV FLUENTD_VERSION 0.14.8  
RUN scl enable rh-ruby23 'gem update --system --no-document' && \  
scl enable rh-ruby23 'gem install --no-document json_pure jemalloc' && \  
scl enable rh-ruby23 "gem install --no-document fluentd -v ${FLUENTD_VERSION}"
&& \  
ln -s /opt/rh/rh-ruby23/root/usr/local/bin/* /usr/bin  
  
MAINTAINER Jimmi Dyson <jimmidyson@gmail.com>  
  
  
ENV ELASTICSEARCH_HOST es-logging.default.svc  
  
RUN touch /var/lib/rpm/* && yum install -y gcc-c++ && yum clean all  
  
RUN scl enable rh-ruby23 'gem install --no-document fluent-plugin-
kubernetes_metadata_filter -v 0.26.2' && \  
scl enable rh-ruby23 'gem install --no-document fluent-plugin-elasticsearch -v
1.7.0' && \  
scl enable rh-ruby23 'gem install --no-document fluent-plugin-prometheus -v
0.2.1' && \  
scl enable rh-ruby23 'gem cleanup fluentd'  
  
ADD start-fluentd /start-fluentd  
ENTRYPOINT ["/start-fluentd"]  

