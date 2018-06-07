FROM debian:jessie  
LABEL maintainer="Paul Howell <paul.howell+docker@gmail.com>"  
  
RUN set -eux && \  
apt-get update && \  
apt-get install -y curl && \  
VERSION=`curl -s https://github.com/Yelp/dumb-init/releases/latest | sed
's/.*tag\/v\\([0-9.]*\\).*/\1/'` && \  
curl -sSL https://github.com/Yelp/dumb-
init/releases/download/v${VERSION}/dumb-init_${VERSION}_amd64 >
/usr/local/bin/dumb-init && \  
chmod +x /usr/local/bin/dumb-init && \  
apt-get remove -y curl  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  

