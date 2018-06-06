# Apline Linux minimal image  
FROM alpine:edge  
  
# default entry point, command and directory  
ENTRYPOINT ["sandbox-run"]  
CMD ["-h"]  
WORKDIR /vol  
  
# add testing repo for libseccomp-dev, then add packages for building and
interpreters for running  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --update \  
gcc \  
libc-dev \  
libseccomp-dev \  
linux-headers \  
make \  
nodejs \  
python \  
ruby  
  
# compile source to binary  
COPY ./src /usr/src/sandbox-run  
RUN cd /usr/src/sandbox-run/ && \  
chmod 644 * && \  
make clean all && \  
mv ./sandbox-run /usr/bin/ && \  
cd .. && \  
rm -rf /usr/src/sandbox-run/  

