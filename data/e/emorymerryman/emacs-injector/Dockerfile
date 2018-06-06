FROM alpine:3.4  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
COPY run.sh entrypoint.sh program.sh /opt/docker/  
RUN ["/bin/sh", "/opt/docker/run.sh"]  
ENV EMACS_IMAGE="emorymerryman/emacs:0.0.1"  
ENTRYPOINT ["/bin/sh", "/opt/docker/entrypoint.sh"]  
CMD ["bin"]

