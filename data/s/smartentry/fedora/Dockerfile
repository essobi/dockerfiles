FROM fedora  
  
MAINTAINER Yifan Gao <docker@yfgao.com>  
  
ENV ASSETS_DIR="/opt/smartentry/HEAD"  
RUN dnf install -y tar && dnf clean all  
  
COPY smartentry.sh /sbin/smartentry.sh  
  
ENTRYPOINT ["/sbin/smartentry.sh"]  
  
CMD ["run"]  

