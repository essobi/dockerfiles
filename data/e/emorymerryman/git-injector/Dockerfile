FROM alpine:3.4  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
COPY run.sh entrypoint.sh program.sh /opt/docker/  
RUN ["/bin/sh", "/opt/docker/run.sh"]  
ENV GIT_IMAGE="emorymerryman/git:0.0.0"  
ENTRYPOINT ["/bin/sh", "/opt/docker/entrypoint.sh"]

