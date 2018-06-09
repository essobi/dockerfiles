FROM httpd  
  
ENV SVN_PREFIX /usr/local/subversion  
RUN mkdir -p "$SVN_PREFIX"  
WORKDIR $SVN_PREFIX  
  
RUN apt-get update \  
&& apt-get install -y libsqlite3-0 libaprutil1-ldap \  
&& rm -r /var/lib/apt/lists/*  
  
ENV SVN_VERSION 1.9.2  
ENV SVN_BZ2_URL
http://mirrors.cnnic.cn/apache/subversion/subversion-$SVN_VERSION.tar.bz2  
  
RUN buildDeps=' \  
ca-certificates \  
curl \  
bzip2 \  
gcc \  
libapr1-dev \  
libaprutil1-dev \  
libc6-dev \  
libsqlite3-dev \  
zlib1g-dev \  
make \  
' \  
set -x \  
&& apt-get update \  
&& apt-get install -y $buildDeps \  
&& rm -r /var/lib/apt/lists/*  
  
RUN curl -SL "$SVN_BZ2_URL" -o subversion.tar.bz2 \  
&& mkdir -p src/subversion \  
&& tar -xvf subversion.tar.bz2 -C src/subversion --strip-components=1 \  
&& rm subversion.tar.bz2 \  
&& cd src/subversion \  
&& ./configure --prefix=$SVN_PREFIX \--with-apxs=$HTTPD_PREFIX/bin/apxs \  
&& make \  
&& make install \  
&& cd ../../ \  
&& rm -r src/subversion \  
&& sed -i 's|#LoadModule dav_module|LoadModule dav_module|g'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#Include conf/extra/httpd-default.conf$|&\n\nInclude
conf/extra/httpd-svn.conf|' /usr/local/apache2/conf/httpd.conf \  
&& echo "LoadModule dav_svn_module $SVN_PREFIX/libexec/mod_dav_svn.so" >>
/usr/local/apache2/conf/extra/httpd-svn.conf \  
&& echo "LoadModule authz_svn_module $SVN_PREFIX/libexec/mod_authz_svn.so" >>
/usr/local/apache2/conf/extra/httpd-svn.conf \  
&& apt-get purge -y --auto-remove $buildDeps  
  
WORKDIR $HTTPD_PREFIX  
  
RUN cp -r /usr/local/apache2/conf /tmp/httpd-conf  
  
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh  
RUN chmod +x /usr/local/sbin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]  
EXPOSE 80  
CMD ["httpd-foreground"]

