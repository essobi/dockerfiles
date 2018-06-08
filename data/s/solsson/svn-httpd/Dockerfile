  
FROM solsson/httpd-
stretch@sha256:5e5359fd904cf2436b6b6811523cf3f0a0bb89eeaa62c667b6d7df901f25d06e  
  
ENV SVN_VERSION 1.8.19  
ENV SVN_BZ2_URL
https://www.apache.org/dist/subversion/subversion-$SVN_VERSION.tar.bz2  
ENV SVN_BZ2_SHA1 51d7e5329ad86a650f8fc806eb68e581055a3fd1  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN depsRuntime=" \  
libsqlite3-0 \  
curl \  
ca-certificates \  
libserf-1-1 \  
" \  
&& depsBuild=" \  
ca-certificates \  
bzip2 \  
gcc \  
libpcre++-dev \  
libssl-dev=$OPENSSL_VERSION \  
make \  
libsqlite3-dev \  
zlib1g-dev \  
libneon27-dev \  
libserf-dev \  
" \  
set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $depsRuntime \  
&& apt-get install -y --no-install-recommends $depsBuild \  
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
&& apt-get purge -y --auto-remove $depsBuild \  
&& rm -r /var/lib/apt/lists/* \  
&& echo "Include conf/svn/httpd.conf" >> conf/httpd.conf  
  
COPY conf conf/svn  
  
# TODO is there a licensing aspect on copy from project source instead of
downloading from docker build?  
COPY site_perl /usr/local/lib/site_perl  
COPY bin/* admin-cgi/  
RUN ln -s $(pwd)/admin-cgi/repocreate /usr/local/bin/repocreate  
  
# Set to non-empty to enable /admin/repocreate http endpoint  
ENV ADMIN_REST_ACCESS ""  
# httpd config has hard coded /svn for parent path, but if we declare a Volume
here you can't prepare repositories in downstream images  
#VOLUME /svn  
RUN mkdir /svn && chown daemon /svn  
  
# Env requires wrapper entrypoint, which we abandoned in
https://github.com/solsson/docker-library-httpd/tree/stretch  
# Set to "anon" to pick up username (for commit log etc) from BASIC auth
header without verification of credentials  
#ENV AUTHN ""  
# Set to "svn"/"inrepo"/"admrepo", see conf/authz/options.conf  
#ENV AUTHZ ""  
# Set to "fpm" to enable rweb conf  
#ENV RWEB ""  
CMD [ "-DAUTHN=", "-DAUTHZ=", "-DRWEB=" ]  

