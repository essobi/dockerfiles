FROM emorymerryman/base:0.0.0  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
COPY run.sh entrypoint.sh /opt/docker/  
RUN ["/bin/sh", "/opt/docker/run.sh"]  
WORKDIR /usr/local/src  
ENTRYPOINT ["/bin/sh", "/opt/docker/entrypoint.sh"]  
CMD []

