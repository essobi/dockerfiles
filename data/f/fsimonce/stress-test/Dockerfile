FROM fedora:latest  
MAINTAINER Federico Simoncelli <fsimonce@redhat.com>  
  
RUN dnf install -y procps-ng stress && dnf clean all  
ADD toprc /root/.toprc  
  
ENV REFRESH_INTERVAL 20  
CMD ["sh", "-c", "exec top -b -d $REFRESH_INTERVAL"]  

