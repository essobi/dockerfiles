FROM debian:stable-slim  
LABEL maintainer="Jean-Avit Promis docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-latest"  
LABEL version="latest"  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install
curl jq ca-certificates && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY latest.sh /latest  
RUN chmod +x /latest  
  
VOLUME /root/latest  
  
ENTRYPOINT [ "/latest" ]  

