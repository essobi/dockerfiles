FROM alpine:3.4  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
COPY run.sh entrypoint.sh program.sh /opt/docker/  
RUN ["/bin/sh", "/opt/docker/run.sh"]  
ENV GPG_IMAGE="emorymerryman/gpg:0.0.0" DOT_GNUPG="dot_gnupg"  
ENTRYPOINT ["/bin/sh", "/opt/docker/entrypoint.sh"]  
CMD []  

