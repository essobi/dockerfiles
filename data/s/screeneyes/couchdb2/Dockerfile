FROM ubuntu:14.04  
MAINTAINER Pablo Maurer  
  
# add couchdb role and user  
RUN groupadd -r couchdb && useradd -d /usr/src/couchdb -g couchdb couchdb  
  
# install needed software  
RUN apt-get update -y -qq && apt-get install -y --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
erlang-dev \  
erlang-nox \  
erlang-reltool \  
git \  
haproxy \  
libcurl4-openssl-dev \  
libicu-dev \  
libmozjs185-dev \  
openssl \  
python  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get update -y -qq && apt-get install -y nodejs \  
&& npm install -g grunt-cli  
  
# clone and make couchdb  
RUN cd /usr/src && git clone \--depth 1 https://git-wip-
us.apache.org/repos/asf/couchdb.git \  
&& cd couchdb && git checkout master \  
&& cd /usr/src/couchdb && ./configure --disable-docs && make && make install \  
&& cd /usr/local/lib/couchdb/etc && sed -i 's/-name couchdb/-name
couchdb@127.0.0.1/g' vm.args  
  
# todo: make available as a service  
# && ln -s /usr/local/etc/init.d/couchdb /etc/init.d  
# update-rc.d couchdb defaults  
# todo remove build and use installed as entrypoint  
# && rm -rf /usr/src/couchdb \  
# cleanup  
RUN apt-get install -y \  
binutils \  
build-essential \  
cpp \  
erlang-dev \  
erlang-reltool \  
libicu-dev \  
make \  
perl  
  
# cleanup  
RUN apt-get autoremove -y && apt-get clean \  
&& apt-get install -y libicu52 --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* /usr/lib/node_modules src/fauxton/node_modules
src/**/.git .git  
  
# change permission  
RUN chmod +x /usr/src/couchdb/dev/run && chown -R couchdb:couchdb
/usr/src/couchdb  
  
# go  
USER couchdb  
EXPOSE 5984 15984 25984 35984 15986 25986 35986  
WORKDIR /usr/src/couchdb  
  
ENTRYPOINT ["/usr/src/couchdb/dev/run"]  
CMD ["--with-haproxy"]

