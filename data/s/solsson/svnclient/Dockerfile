FROM
debian:jessie@sha256:f7062cf040f67f0c26ff46b3b44fe036c29468a7e69d8170f37c57f2eec1261b  
  
ENV SVN_VERSION 1.9.5  
ENV SVN_BZ2_URL
https://www.apache.org/dist/subversion/subversion-$SVN_VERSION.tar.bz2  
ENV SVN_BZ2_SHA1 8bd6a44a1aed30c4c6b6b068488dafb44eaa6adf  
  
RUN depsRuntime=' \  
libsqlite3-0 \  
ca-certificates \  
curl \  
libapr1 \  
libaprutil1 \  
libneon27 \  
libserf-1-1 \  
' \  
&& depsBuild=' \  
bzip2 \  
gcc \  
libpcre++-dev \  
libssl-dev \  
make \  
libsqlite3-dev \  
libz-dev \  
libapr1-dev \  
libaprutil1-dev \  
libneon27-dev \  
libserf-dev \  
' \  
set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $depsRuntime \  
&& apt-get install -y --no-install-recommends $depsBuild \  
&& rm -r /var/lib/apt/lists/* \  
&& curl -SL "$SVN_BZ2_URL" -o subversion-$SVN_VERSION.tar.bz2 \  
&& echo "$SVN_BZ2_SHA1 subversion-$SVN_VERSION.tar.bz2" | sha1sum -c - \  
&& mkdir -p src/svn \  
&& tar -xvf subversion-$SVN_VERSION.tar.bz2 -C src/svn --strip-components=1 \  
&& rm subversion-$SVN_VERSION.tar.bz2* \  
&& cd src/svn \  
&& ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& /sbin/ldconfig \  
&& cd ../../ \  
&& rm -r src/svn \  
&& apt-get purge -y --auto-remove $depsBuild  

