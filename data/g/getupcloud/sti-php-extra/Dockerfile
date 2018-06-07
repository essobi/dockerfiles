FROM centos/php-56-centos7:latest  
  
USER root  
  
ENV NPM_CONFIG_PREFIX=$HOME/.npm-global \  
PATH=$HOME/node_modules/.bin/:$HOME/.npm-
global/bin/:$PATH:/usr/local/bin/ffmpeg/  
  
RUN yum install -y centos-release-scl-rh && \  
INSTALL_PKGS="glibc-common more-php56-php-pecl-redis more-php56-php-mcrypt
newrelic-php5 nss_wrapper sclo-php56-php-pecl-imagick" && \  
yum install -y
https://www.softwarecollections.org/en/scls/remi/php56more/epel-7-x86_64/download/remi-
php56more-epel-7-x86_64.noarch.rpm && \  
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
yum install -y http://yum.newrelic.com/pub/newrelic/el5/x86_64/newrelic-
repo-5-3.noarch.rpm && \  
yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && NR_INSTALL_SILENT=1
newrelic-install install && \  
yum clean all -y && \  
cd /opt/rh/httpd24/root && \  
curl https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-
stable_current_x86_64.rpm | rpm2cpio | cpio -idvm && rm -f
/opt/rh/httpd24/root/etc/httpd/conf.d/pagespeed.conf  
  
ENV NODE_VERSION=8.4.0 \  
ARCH=x64  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" && \  
tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 && \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \  
npm install -g nodemon  
  
#====================================================================  
# ffmpeg  
ENV FFMPEG_VERSION 3.0  
ENV SRC /usr/local  
RUN DIR=$(mktemp -d) && cd /tmp && \  
curl -Os http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz && \  
tar xzvf ffmpeg-${FFMPEG_VERSION}.tar.gz && \  
cd ffmpeg-${FFMPEG_VERSION} && \  
./configure --prefix="${SRC}" \--extra-cflags="-I${SRC}/include" \--extra-
ldflags="-L${SRC}/lib" \--bindir="${SRC}/bin" \  
\--extra-libs=-ldl --enable-version3 --enable-gpl \  
\--enable-postproc --enable-nonfree --enable-avresample --disable-debug
--enable-small --disable-yasm && \  
make && \  
make install && \  
make distclean && \  
hash -r && \  
rm -rf ${DIR}  
#====================================================================  
#PhantomJS 2.1.1  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& tar -xjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/bin/ && mv
/usr/local/bin/phantomjs-2.1.1-linux-x86_64 /usr/local/bin/phantomjs && rm -f
phantomjs-2.1.1-linux-x86_64.tar.bz2  
  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
COPY ./contrib/ /opt/app-root  
  
RUN rm -rf /opt/rh/httpd24/root/var/run/httpd && mkdir -p
/opt/rh/httpd24/root/var/run/httpd  
  
RUN chmod -R a+rwx /opt/rh/httpd24/root/etc/httpd/conf.d && \  
chown -R 1001:0 /opt/app-root /tmp/sessions && \  
chmod -R a+rwx /tmp/sessions && \  
chmod -R ug+rwx /opt/app-root && \  
chmod -R a+rwx /etc/opt/rh/rh-php56/php.d && \  
chmod -R a+rwx /opt/rh/httpd24/root/etc/httpd/conf.d && \  
chmod -R a+rwx /opt/rh/httpd24/root/var/run/httpd  
  
USER 1001  

