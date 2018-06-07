FROM buildpack-deps:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
unzip \  
vim \  
supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG C.UTF-8  
#-------------------------------------------------------------------------  
# python  
ENV PYTHON_VERSION 3.5.2  
ENV PYTHON_PIP_VERSION 8.1.2  
RUN set -ex \  
&& buildDeps=' \  
tcl-dev \  
tk-dev \  
' \  
&& runDeps=' \  
tcl \  
tk \  
' \  
# gpg: key F73C700D: public key "Larry Hastings <larry@hastings.org>" imported  
&& GPG_KEY=97FC712E4C024BBEA48A61ED3A5CA953F73C700D \  
&& apt-get update && apt-get install -y $runDeps $buildDeps --no-install-
recommends && rm -rf /var/lib/apt/lists/* \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& ./configure \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& pip3 install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \  
&& [ "$(pip list | awk -F '[ ()]+' '$1 == "pip" { print $2; exit }')" =
"$PYTHON_PIP_VERSION" ] \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /usr/src/python ~/.cache  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s easy_install-3.5 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
#-------------------------------------------------------------------------  
# perl  
ENV PERL_VERSION 5.24.0  
RUN mkdir /usr/src/perl  
COPY *.patch /usr/src/perl/  
  
RUN cd /usr/src/perl \  
&& curl -SL
https://cpan.metacpan.org/authors/id/R/RJ/RJBS/perl-$PERL_VERSION.tar.bz2 -o
perl-$PERL_VERSION.tar.bz2 \  
&& echo '298fa605138c1a00dab95643130ae0edab369b4d *perl-5.24.0.tar.bz2' |
sha1sum -c - \  
&& tar --strip-components=1 -xjf perl-$PERL_VERSION.tar.bz2 -C /usr/src/perl \  
&& rm perl-$PERL_VERSION.tar.bz2 \  
&& cat *.patch | patch -p1 \  
&& ./Configure -Duse64bitall -Duseshrplib -des \  
&& make -j$(nproc) \  
&& TEST_JOBS=$(nproc) make test_harness \  
&& make install \  
&& cd /usr/src \  
&& curl -LO https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
\  
&& chmod +x cpanm \  
&& ./cpanm App::cpanminus \  
&& rm -fr ./cpanm /root/.cpanm /usr/src/perl /tmp/*  
  
#-------------------------------------------------------------------------  
# node.js  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.3.1  
RUN set -e \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
#-------------------------------------------------------------------------  
# java  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV JAVA_VERSION 8u91  
ENV JAVA_DEBIAN_VERSION 8u91-b14-1~bpo8+1  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20140324  
RUN apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
  
#-------------------------------------------------------------------------  
# ruby  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.1  
ENV RUBY_DOWNLOAD_SHA256
b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd  
ENV RUBYGEMS_VERSION 2.6.6  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN set -e \  
&& buildDeps=' \  
bison \  
libgdbm-dev \  
ruby \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/ruby \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new &&
mv file.c.new file.c \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
ENV BUNDLER_VERSION 1.12.5  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
#-------------------------------------------------------------------------  
# golang  
ENV GOLANG_VERSION 1.6.3  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
cdde5e08530c0579255d6153b08fdb3b8e47caabbe717bc7bcd7561275a87aeb  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  

