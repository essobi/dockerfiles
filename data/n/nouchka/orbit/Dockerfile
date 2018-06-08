FROM debian:stable-slim  
LABEL maintainer="Jean-Avit Promis docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-orbit"  
LABEL version="latest"  
  
ARG PUID=1000  
ARG PGID=1000  
ENV PUID ${PUID}  
ENV PGID ${PGID}  
  
ARG ORBIT_VERSION=2.0.0  
ARG
ORBIT_FILE_SHA256SUM=47d78353d1f17a5c9cb53ac3e97a515f9fef4654b67cfbb8bfdbaefe2e880a40  
  
WORKDIR /tmp  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install
wget tar ca-certificates && \  
wget -qO-
"https://github.com/gulien/orbit/releases/download/v${ORBIT_VERSION}/orbit_Linux_x86_64.tar.gz"|
tar xzf - -C / && \  
sha256sum /orbit && \  
echo "${ORBIT_FILE_SHA256SUM} /orbit"| sha256sum -c - && \  
chmod +x /orbit && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
export uid=${PUID} gid=${PGID} && \  
mkdir -p /home/developer/orbit && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
chown "${uid}:${gid}" -R /home/developer  
  
VOLUME /home/developer/orbit  
WORKDIR /home/developer/orbit  
  
ENTRYPOINT [ "/orbit" ]  

