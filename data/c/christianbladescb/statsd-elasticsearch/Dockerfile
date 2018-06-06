FROM quay.io/assemblyline/ubuntu:14.04.2  
MAINTAINER Christian Blades <christian.blades@careerbuilder.com>  
  
ADD http://nodejs.org/dist/v0.12.1/node-v0.12.1-linux-x64.tar.gz /tmp/node.tgz  
ADD https://github.com/etsy/statsd/archive/v0.7.2.tar.gz /tmp/statsd.tgz  
ADD https://github.com/markkimsal/statsd-elasticsearch-
backend/archive/0.2.0.tar.gz /tmp/statsd-elasticsearch.tgz  
  
RUN mkdir -p /app  
WORKDIR /app  
  
# install node  
RUN cd /tmp; \  
tar xzf /tmp/node.tgz; \  
mv /tmp/node-v0.12.1-linux-x64/bin/* /usr/local/bin/; \  
mv /tmp/node-v0.12.1-linux-x64/include/* /usr/local/include/; \  
mv /tmp/node-v0.12.1-linux-x64/lib/* /usr/local/lib/; \  
rm /tmp/node.tgz  
  
# build prerequisites  
RUN apt-get update; DEBIAN_FRONTEND=noninteractive apt-get install -q -y
python-minimal build-essential  
  
# install statsd and the elasticsearch plugin  
RUN npm install /tmp/statsd.tgz; rm /tmp/statsd.tgz  
RUN npm install /tmp/statsd-elasticsearch.tgz; rm /tmp/statsd-
elasticsearch.tgz  
  
# cleanup build prerequisites  
RUN apt-get remove -qy --purge \  
binutils build-essential bzip2 cpp cpp-4.8 dpkg-dev fakeroot file g++ \  
g++-4.8 gcc gcc-4.8 libalgorithm-diff-perl libalgorithm-diff-xs-perl \  
libalgorithm-merge-perl libarchive-extract-perl libasan0 libatomic1 \  
libc-dev-bin libc6-dev libcloog-isl4 libdpkg-perl libexpat1 libfakeroot \  
libffi6 libfile-fcntllock-perl libgcc-4.8-dev libgdbm3 libgmp10 libgomp1 \  
libisl10 libitm1 liblog-message-simple-perl libmagic1 \  
libmodule-pluggable-perl libmpc3 libmpfr4 libpod-latex-perl libpython-stdlib \  
libpython2.7-minimal libpython2.7-stdlib libquadmath0 libsqlite3-0 \  
libssl1.0.0 libstdc++-4.8-dev libterm-ui-perl libtext-soundex-perl \  
libtimedate-perl libtsan0 linux-libc-dev make manpages manpages-dev \  
mime-support patch perl perl-modules python python-minimal python2.7 \  
python2.7-minimal xz-utils  
RUN apt-get -qy autoremove; apt-get -qy autoclean  
  
ADD ./config.js /app/  
  
CMD $(npm bin)/statsd /app/config.js  
  
EXPOSE 8125/udp 8126  

