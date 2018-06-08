FROM
php:7.1.5-fpm@sha256:2256f2bd134274434814c394002b4e11802e02aa554ef197741705d83523fd59  
  
# Same build concept as in httpd,  
# but rweb should only have the svn client with http ra  
  
ENV SVN_VERSION 1.8.17  
ENV SVN_BZ2_URL
https://www.apache.org/dist/subversion/subversion-$SVN_VERSION.tar.bz2  
ENV SVN_BZ2_SHA1 0999f5e16b146f824b952a5552826b9cb5c47b13  
  
RUN buildDeps=' \  
ca-certificates \  
curl \  
bzip2 \  
gcc \  
libpcre++-dev \  
make \  
libsqlite3-dev \  
libz-dev \  
libapr1-dev \  
libaprutil1-dev \  
libserf-dev \  
libneon27-dev \  
' \  
set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends libsqlite3-0 libapr1 libserf-1-1
libneon27 \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -r /var/lib/apt/lists/* \  
&& curl -SL "$SVN_BZ2_URL" -o subversion-$SVN_VERSION.tar.bz2 \  
&& echo "$SVN_BZ2_SHA1 subversion-$SVN_VERSION.tar.bz2" | sha1sum -c - \  
&& mkdir -p src/svn \  
&& tar -xvf subversion-$SVN_VERSION.tar.bz2 -C src/svn --strip-components=1 \  
&& rm subversion-$SVN_VERSION.tar.bz2* \  
&& cd src/svn \  
&& ./configure \  
\--with-serf \  
\--without-gpg-agent \  
\--without-berkeley-db \  
\--without-apxs \  
\--without-swig \  
&& make -j"$(nproc)" \  
&& make install \  
&& cd ../../ \  
&& rm -r src/svn \  
&& apt-get purge -y --auto-remove $buildDeps  

