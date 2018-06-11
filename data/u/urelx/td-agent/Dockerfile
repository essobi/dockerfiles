FROM centos:centos6  
MAINTAINER Yuu Yamanaka <yuu@relx.jp>  
  
RUN yum update -y  
  
ADD td.repo /etc/yum.repos.d/  
RUN yum install -y td-agent  
RUN echo "include /conf.d/*.conf" > /etc/td-agent/td-agent.conf  
  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN /usr/lib64/fluent/ruby/bin/gem install fluent-plugin-file-alternative  
RUN /usr/lib64/fluent/ruby/bin/gem install fluent-plugin-forest  
RUN /usr/lib64/fluent/ruby/bin/gem install fluent-plugin-tail-asis  
RUN /usr/lib64/fluent/ruby/bin/gem install fluent-plugin-multiprocess  
  
VOLUME ["/conf.d", "/data"]  
EXPOSE 24224/tcp 24224/udp  
  
ENTRYPOINT ["td-agent"]  

