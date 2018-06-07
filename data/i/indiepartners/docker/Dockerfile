FROM fedora:26  
LABEL maintainer="claude@indie-partners.com"  
  
RUN set -ex; \  
echo 'fastestmirror=true' >> /etc/dnf/dnf.conf; \  
dnf update -q --setopt=install_weak_deps=False -y; \  
dnf install -q --nodocs --setopt=install_weak_deps=False -y wget curl;  

