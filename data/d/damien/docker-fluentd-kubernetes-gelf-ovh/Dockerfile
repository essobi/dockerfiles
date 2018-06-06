FROM fabric8/fluentd:0.14.8  
ENTRYPOINT ["fluentd"]  
  
RUN yum install -y curl-dev wget gcc-c++  
  
RUN scl enable rh-ruby23 'gem install fluent-plugin-kubernetes_metadata_filter
fluent-plugin-forest gelf'  
  
RUN mkdir -p /etc/fluent/plugin  
  
ENV GELF_HOST discover.logs.ovh.com  
ENV GELF_PORT 12202  
ENV GELF_PROTOCOL tcp  
ENV GELF_TLS true  
ENV OVH_TOKEN DEFAULT  
  
ADD out_gelf.rb /etc/fluent/plugin/out_gelf.rb  
ADD fluent.conf /etc/fluent/fluent.conf  

