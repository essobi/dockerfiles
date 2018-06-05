FROM centos:7  
MAINTAINER Chris Machler <chris.machler@evergreenitco.com>  
  
ENV LD_LIBRARY_PATH /opt/rh/rh-ruby23/root/usr/lib64  
ENV FLUENTD_VERSION 0.14.12  
RUN yum update -y && \  
yum install -y centos-release-scl-rh && \  
yum install -y scl-utils make gcc gcc-c++ bzip2 rh-ruby23 rh-ruby23-ruby-devel
&& \  
scl enable rh-ruby23 'gem update --system --no-document' && \  
scl enable rh-ruby23 'gem install --no-document json_pure jemalloc' && \  
scl enable rh-ruby23 "gem install --no-document fluentd -v ${FLUENTD_VERSION}"
&& \  
scl enable rh-ruby23 "gem install --no-document fluent-plugin-
kubernetes_metadata_filter fluent-plugin-forest fluent-plugin-systemd fluent-
plugin-secure-forward" && \  
ln -s /opt/rh/rh-ruby23/root/usr/local/bin/* /usr/bin && \  
yum remove -y rh-ruby23-ruby-devel-2.3.0-60 glibc-devel-2.17-106.el7_2.8
libstdc++-devel-4.8.5-4.el7.x86_64 make gcc gcc-c++ bzip2 rh-ruby23-ruby-devel
&& \  
yum clean all  
  
ADD fluent.conf /etc/fluent/fluent.conf  
  
CMD ["je", "fluentd"]  

