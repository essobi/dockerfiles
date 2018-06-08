FROM fedora:25  
LABEL maintainer "speg03@gmail.com"  
  
# Install Packages  
RUN dnf update -y && dnf clean all  
ADD ./packages.list /build/  
RUN dnf install -y findutils  
RUN cat /build/packages.list | grep -v '^#' | grep -v '^$' \  
| xargs dnf install -y && dnf clean all  
  
# Set timezone to Asia/Tokyo  
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
EXPOSE 22  
ADD ./run.sh /build/  
ENTRYPOINT ["/build/run.sh"]  

