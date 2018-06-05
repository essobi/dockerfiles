FROM golang:1.9-alpine  
  
WORKDIR /data  
  
RUN apk add --no-cache \  
ca-certificates &&\  
update-ca-certificates  
  
# Install build dependencies (permanently since we are going to keep the  
# ability to install additional plugins which will require a complete Caddy  
# rebuild)  
RUN apk add --no-cache --virtual build-deps \  
bash \  
gcc \  
git \  
xz  
  
# Preconfiguration  
RUN \  
git config --global http.followRedirects true &&\  
mkdir -vp "${GOPATH}"  
  
# Add the scripts  
COPY files/ /usr/local/  
# Fix permissions and line endings in case we use `docker build` from Windows  
# because remember, Docker client can run on Windows despite the host running  
# on Linux!  
RUN \  
chmod -v +x /usr/local/bin/* &&\  
sed -i 's,\r,,g' /usr/local/bin/*  
  
# Install Caddy itself  
ARG CADDY_VERSION=v0.10.10  
RUN \  
echo "*** Fetching Caddy..." &&\  
git clone \--recursive "https://github.com/mholt/caddy.git" \  
"$GOPATH/src/github.com/mholt/caddy" &&\  
git clone \--recursive "https://github.com/caddyserver/builds.git" \  
"$GOPATH/src/github.com/caddyserver/builds" &&\  
(cd "$GOPATH/src/github.com/mholt/caddy" &&\  
git checkout "$CADDY_VERSION") &&\  
docker-caddy-build &&\  
docker-caddy-pack-source  
  
# I would have run "setcap cap_net_bind_service=+ep /usr/local/bin/caddy" as
well but it will not work in Docker  
# thanks to inconsistencies with aufs and kernel settings on Ubuntu.  
#  
# My recommendation is to let Caddy bind to a non-root port instead and use
the Docker userland proxy if possible,  
# so for example binding Caddy to port 2200 and telling Docker to forward port
80 to port 2200 in the container  
# should be just fine.  
WORKDIR /data  
ENTRYPOINT ["caddy"]  
CMD ["-agree"]  

