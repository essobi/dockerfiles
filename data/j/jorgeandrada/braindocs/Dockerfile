FROM gliderlabs/alpine:latest  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Braindocs" \  
org.label-schema.description="Braindocs: Mkdocs auto public server." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/braindocs" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --rm -it --name braindocs -v
mkdocs_local_path:/root/mkdocs -p 8000:80 jorgeandrada/braindocs"  
  
RUN apk add --update python3 py-pip && \  
pip install --upgrade pip && \  
pip3 install --upgrade pip && \  
pip3 install mkdocs && \  
rm -rf /var/cache/apk/*  
  
COPY . /root/mkdocs  
  
WORKDIR /root/mkdocs  
  
EXPOSE 80  
  
ENTRYPOINT ["/usr/bin/mkdocs", "serve", "--dev-addr=0.0.0.0:80"]  

