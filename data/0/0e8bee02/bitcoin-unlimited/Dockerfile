FROM alpine:3.5  
  
ARG BERKELEYDB_VERSION=4.8.30  
ARG BITCOIN_UNLIMITED_VERSION=1.0.0.1  
ARG SUPERVISOR_VERSION=3.3.0  
  
WORKDIR /srv/src  
  
COPY supervisord.conf /etc/  
COPY entrypoint.sh .  
  
RUN apk update \  
&& apk add --no-cache --virtual build-dependencies \  
git build-base \  
automake \  
autoconf \  
libtool \  
boost-dev \  
openssl-dev \  
libevent-dev \  
tor \  
py-pip \  
  
&& wget http://download.oracle.com/berkeley-db/db-${BERKELEYDB_VERSION}.tar.gz
\  
&& tar -xzf db-${BERKELEYDB_VERSION}.tar.gz \  
&& cd db-${BERKELEYDB_VERSION}/build_unix \  
&& ../dist/configure --enable-cxx --prefix /usr/local \  
&& make install \  
  
&& cd /srv/src \  
&& git clone https://github.com/BitcoinUnlimited/BitcoinUnlimited.git \  
&& cd BitcoinUnlimited \  
&& git checkout tags/${BITCOIN_UNLIMITED_VERSION} \  
  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& pip install --upgrade pip \  
&& pip install supervisor==$SUPERVISOR_VERSION \  
  
&& cd /srv/src \  
&& chmod +x entrypoint.sh \  
  
&& printf "%s\n%s\n%s\n%s\n%s\n" \  
"ControlPort 9051" \  
"CookieAuthentication 1" \  
"CookieAuthFileGroupReadable 1" \  
>> /etc/tor/torrc  
  
VOLUME ["/root/.bitcoin"]  
  
EXPOSE 8333  
EXPOSE 9050  
  
CMD ["./entrypoint.sh"]  

