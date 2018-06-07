FROM fedora:22  
MAINTAINER James Findley  
  
RUN dnf -y install \  
git \  
ruby \  
gcc \  
gcc-c++ \  
kernel-devel \  
ruby-devel \  
openssl \  
make \  
tzdata \  
ruby \  
ruby-devel \  
rubygems \  
rubygem-uuidtools  
  
RUN gem install --no-ri --no-rdoc fluentd -v 0.12.15  
RUN gem install --no-ri --no-rdoc fluent-plugin-elasticsearch -v 1.0.0  
  
COPY fluent.conf /etc/fluent/fluent.conf  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD fluentd  

