FROM fedora:latest  
MAINTAINER Patrice Ferlet <metal3d@gmail.com>  
  
ENV ADDR 0.0.0.0:8000  
ENV UID 1000  
ENV GID 1000  
RUN dnf install -y gcc patch python-devel python-pip && \  
dnf clean all && \  
pip install mkdocs  
  
# Hack to not use the host:port for livereload  
COPY livereload.patch /livereload.patch  
RUN cd /usr/lib/python2.7/ && patch -p4 < /livereload.patch && cd /  
  
RUN useradd -m mkdocuser  
WORKDIR /mkdocs  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["bash", "/entrypoint.sh"]  
CMD ["serve"]  

