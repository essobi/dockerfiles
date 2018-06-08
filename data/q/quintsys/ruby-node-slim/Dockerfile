FROM ruby:2.5.1-slim  
  
ENV NODE_VERSION='6.x' \  
YARN_VERSION='latest'  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends apt-utils \  
curl \  
build-essential \  
libxml2-dev \  
libxslt1-dev \  
libcurl4-openssl-dev \  
gnupg \  
dirmngr \  
&& curl -sL https://deb.nodesource.com/setup_${NODE_VERSION} | bash \  
&& apt-get install -y --no-install-recommends nodejs \  
&& apt-get upgrade -y \  
&& if [ -n "$YARN_VERSION" ]; then \  
for server in pgp.mit.edu keyserver.pgp.com ha.pool.sks-keyservers.net; do \  
gpg --keyserver $server \--recv-keys \  
6A010C5166006599AA17F08146C2130DFD2497F5 && break; \  
done && \  
curl -sfSL -O https://yarnpkg.com/${YARN_VERSION}.tar.gz -O
https://yarnpkg.com/${YARN_VERSION}.tar.gz.asc && \  
gpg --batch --verify ${YARN_VERSION}.tar.gz.asc ${YARN_VERSION}.tar.gz && \  
mkdir /usr/local/share/yarn && \  
tar -xf ${YARN_VERSION}.tar.gz -C /usr/local/share/yarn --strip 1 && \  
ln -s /usr/local/share/yarn/bin/yarn /usr/local/bin/ && \  
ln -s /usr/local/share/yarn/bin/yarnpkg /usr/local/bin/ && \  
rm ${YARN_VERSION}.tar.gz*; \  
fi \  
&& apt-get purge -y --auto-remove \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["bash"]  

