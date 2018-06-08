FROM debian:stretch  
MAINTAINER Nathan Ostgard <noonat@phuce.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install build dependencies. Note that python is required to build Node.  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
autoconf \  
bison \  
build-essential \  
ca-certificates \  
curl \  
git-core \  
libcurl4-openssl-dev \  
libffi-dev \  
libgdbm3 \  
libgdbm-dev \  
libreadline-dev \  
libncurses5-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
python \  
sqlite3 \  
zlib1g-dev  
  
# Clone everything, and setup the path.  
RUN git clone https://github.com/rbenv/rbenv.git /root/.rbenv && \  
git clone https://github.com/rbenv/ruby-build.git /root/.rbenv/plugins/ruby-
build && \  
git clone https://github.com/nodenv/nodenv.git /root/.nodenv && \  
git clone https://github.com/nodenv/node-build.git /root/.nodenv/plugins/node-
build && \  
git clone https://github.com/nodenv/nodenv-package-rehash.git
/root/.nodenv/plugins/nodenv-package-rehash && \  
git clone https://github.com/nodenv/nodenv-update.git
/root/.nodenv/plugins/nodenv-update  
ENV PATH
/root/.rbenv/shims:/root/.rbenv/bin:/root/.nodenv/shims:/root/.nodenv/bin:$PATH  
  
CMD ["/bin/bash"]  

