FROM centos:7  
MAINTAINER Giles Thomas <giles@lemonman.org.uk>  
  
RUN yum -y update && \  
yum clean all  
  
RUN useradd -ms /bin/bash pixelserv  
COPY pixelserv.py /pixelserv.py  
RUN chmod 755 /pixelserv.py  
  
USER pixelserv  
  
EXPOSE 8000  
CMD ["python", "-u", "/pixelserv.py"]  
  

