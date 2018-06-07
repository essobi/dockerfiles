# cunnie/fedora-golang-bosh  
FROM fedora:25  
MAINTAINER Brian Cunnie <brian.cunnie@gmail.com>  
  
# need ruby to run dns-check.rb & bind-utils for dig & nslookup  
RUN dnf update -y; \  
dnf groupinstall -y "Development Tools"; \  
dnf install -y golang; \  
dnf install -y ruby rubygems ruby-devel redhat-rpm-config; \  
dnf install -y mysql-devel openssl-devel zlib-devel; \  
gem install yajl-ruby  
  
RUN curl -L https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.40-linux-
amd64 -o /usr/local/bin/bosh; \  
chmod +x /usr/local/bin/bosh  

