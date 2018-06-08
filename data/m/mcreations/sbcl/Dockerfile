## -*- docker-image-name: "mcreations/sbcl" -*-  
  
FROM mcreations/openwrt-x64  
MAINTAINER Kambiz Darabi <darabi@m-creations.net>  
  
ENV SBCL_VERSION 1.4.1-101-ga860f4780~zesty+2  
  
ENV DOWNLOAD_URL https://launchpad.net/~darabi/+archive/ubuntu/lisp/+files  
  
ENV DOWNLOAD_PACKAGE sbcl_${SBCL_VERSION}_amd64.deb  
  
ENV SHA256_SUM
1d5cde1fe824f2ff9560600bfb657fec7b864a5c362d3a3f5003111425818f26  
  
ENV QUICKLISP_HOME /opt/quicklisp  
  
ENV QUICKLISP_VERSION 2017-12-27  
  
ENV MCREATIONS_DIST_VERSION 2018.01.17_22-22-41-GMT  
  
ENV XDG_CACHE_HOME /cache  
  
ENV GOSU_VERSION 1.10  
  
# userid:groupid to run sbcl with  
ENV RUN_AS 1000:1000  
# contains the start-sbcl script and a  
# patch for quicklisp-client's mtime handling  
ADD image/root/ /  
  
RUN opkg update &&\  
opkg install \--force-overwrite \  
ar \  
coreutils-id \  
coreutils-sha256sum \  
coreutils-stat \  
gcc \  
graphviz \  
libffi libffi-dev \  
libfixposix libfixposix-dev \  
libuv libuv-dev \  
make \  
patch \  
rlwrap \  
shadow-groupadd \  
shadow-su \  
shadow-useradd \  
tar \  
xz \  
zoneinfo-core &&\  
rm /etc/localtime &&\  
ln -s /usr/share/zoneinfo/UTC /etc/localtime &&\  
mkdir /home &&\  
cd /tmp &&\  
chmod 1777 . &&\  
wget -O gosu \--progress=dot:giga
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64"
&&\  
chmod a+x gosu &&\  
mv gosu /usr/bin &&\  
wget \--progress=dot:giga $DOWNLOAD_URL/$DOWNLOAD_PACKAGE &&\  
echo "$SHA256_SUM $DOWNLOAD_PACKAGE" | sha256sum -c &&\  
mkdir sbcl-unpack && cd sbcl-unpack &&\  
ar x ../$DOWNLOAD_PACKAGE &&\  
tar xfvJ /tmp/sbcl-unpack/data.tar.xz -C / &&\  
rm -rf /usr/share/{man,doc,lintian,binfmts} &&\  
rm -rf /tmp/sbcl* &&\  
rm /tmp/opkg-lists/* &&\  
cd ~ &&\  
echo "Finished installing SBCL. Now it's time for Quicklisp." &&\  
wget -O /tmp/quicklisp.lisp https://beta.quicklisp.org/quicklisp.lisp &&\  
mkdir /opt &&\  
mkdir -p /common-lisp &&\  
mkdir -p /usr/share/common-lisp &&\  
mkdir -p $XDG_CACHE_HOME &&\  
ln -s /common-lisp /usr/share/common-lisp/source &&\  
echo | sbcl \--load /tmp/quicklisp.lisp \--eval '(quicklisp-quickstart:install
:path "/opt/quicklisp")' \--eval '(quicklisp:add-to-init-file)' \--eval '(sb-
ext:quit)' &&\  
echo | sbcl \--load /opt/quicklisp/setup.lisp \--eval "(ql-dist:install-dist
\"http://beta.quicklisp.org/dist/quicklisp/$QUICKLISP_VERSION/distinfo.txt\"
:replace t)" \  
\--eval "(mapcar #'ql-dist:ensure-local-archive-file (mapcar #'ql-dist:release
(ql-dist:provided-systems (ql-dist:find-dist \"quicklisp\"))))" &&\  
echo | sbcl \--load /opt/quicklisp/setup.lisp \--eval "(ql-dist:install-dist
\"http://ql.m-creations.net/m-creations/$MCREATIONS_DIST_VERSION/distinfo.txt\"
:replace t)" \  
\--eval "(mapcar #'ql-dist:ensure-local-archive-file (mapcar #'ql-dist:release
(ql-dist:provided-systems (ql-dist:find-dist \"m-creations\"))))" &&\  
cd /opt/quicklisp &&\  
patch -p 1 < /tmp/001-minitar-set-file-mtime.patch &&\  
mv /usr/bin/sbcl /usr/bin/sbcl-binary &&\  
mv /usr/bin/start-sbcl /usr/bin/sbcl  
  
  
ENTRYPOINT ["sbcl"]  

