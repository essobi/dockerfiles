FROM fedora:latest  
MAINTAINER Michael Gruener <michael.gruener@chaosmoon.net>  
  
# Available in Fedora but wrong version:  
# rubygem-pry  
# rubygem-launchy  
RUN dnf -y install \  
git \  
rubygem-addressable \  
rubygem-backports \  
rubygem-coderay \  
rubygem-ethon \  
rubygem-faraday \  
rubygem-ffi \  
rubygem-highline \  
rubygem-method_source \  
rubygem-multi_json \  
rubygem-multipart-post \  
rubygem-net-http-persistent \  
rubygem-slop \  
rubygem-typhoeus \  
rubygem-websocket \  
vim && \  
dnf clean all && \  
gem install --clear-sources --no-document travis && \  
gem sources -c  
  
RUN useradd -m travis  
USER travis  
WORKDIR /home/travis  
  
CMD ["/bin/bash"]  

