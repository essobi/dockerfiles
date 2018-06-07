FROM centos  
MAINTAINER Filirom1 <filirom1@gmail.com>  
  
RUN yum install -y epel-release  
RUN yum install -y patch tar git ruby ruby-devel rubygem-bundler make gcc
gcc-c++ zlib-devel libxml2-devel nginx  
  
# optimize layer caching for bundle install  
RUN mkdir -p /tmp/lib/inventory/server  
ADD Gemfile /tmp/Gemfile  
ADD inventory-server.gemspec /tmp/inventory-server.gemspec  
ADD lib/inventory/server/version.rb /tmp/lib/inventory/server/version.rb  
RUN cd /tmp && bundle install  
  
RUN mkdir -p /var/log/inventory && chmod o+rwX /var/log/inventory && \  
mkdir -p /var/lib/inventory/ && chmod o+rwX /var/lib/inventory && \  
mkdir -p /var/run/inventory/ && chmod o+rwX /var/run/inventory  
  
VOLUME ["/var/log/nginx", "/var/log/inventory"]  
  
EXPOSE 80  
ADD . /app  
  
RUN cp /app/docker/unicorn/unicorn.conf /etc/nginx/conf.d/unicorn.conf && \  
cp /app/docker/unicorn/nginx.conf /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
WORKDIR /app  
  
CMD ["/app/docker/unicorn/run-unicorn.sh"]  

