FROM alpine:3.6  
ARG UNISON_VERSION=2.51.2  
# Install in one run so that build tools won't remain in any docker layers  
# Install build tools  
RUN apk add --update build-base curl bash ocaml && \  
# Download & Install Unison  
curl -L https://github.com/bcpierce00/unison/archive/v$UNISON_VERSION.tar.gz |
tar zxv -C /tmp && \  
cd /tmp/unison-${UNISON_VERSION} && \  
sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/'
src/fsmonitor/linux/inotify_stubs.c && \  
make UISTYLE=text NATIVE=true STATIC=true && \  
cp /tmp/unison-${UNISON_VERSION}/src/unison
/tmp/unison-${UNISON_VERSION}/src/unison-fsmonitor /usr/local/bin && \  
# Remove build tools  
apk del build-base curl ocaml && \  
# Remove tmp files and caches  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/unison-${UNISON_VERSION}  
  
# These can be overridden later  
ENV UNISON_DIR="/unison"  
COPY root /  
  
VOLUME $UNISON_DIR  
  
EXPOSE 5000  
ENTRYPOINT ["/opt/bin/entrypoint.sh"]  
CMD /bin/bash  

