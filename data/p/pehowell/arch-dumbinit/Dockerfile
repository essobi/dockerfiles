FROM pritunl/archlinux  
LABEL maintainer="Paul Howell <paul.howell+docker@gmail.com>"  
  
RUN set -euxo pipefail && \  
VERSION=`curl -s https://github.com/Yelp/dumb-init/releases/latest | sed
's/.*tag\/v\\([0-9.]*\\).*/\1/'` && \  
curl -sSL https://github.com/Yelp/dumb-
init/releases/download/v${VERSION}/dumb-init_${VERSION}_amd64 >
/usr/local/bin/dumb-init && \  
chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  

