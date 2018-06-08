FROM buildpack-deps:xenial  
  
###############################################################################  
# Java  
#  
# http://bit.ly/2AVvMJy  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
  
###############################################################################  
# Leiningen/Clojure  
#  
# Ref: http://bit.ly/2AUouWu  
ENV LEIN_VERSION=2.8.1  
ENV LEIN_DOWNLOAD_SHA=019faa5f91a463bf9742c3634ee32fb3db8c47f0  
ENV LEIN_INSTALL=/usr/local/bin/  
  
WORKDIR /tmp  
  
RUN mkdir -p $LEIN_INSTALL \  
&& wget -q
https://raw.githubusercontent.com/technomancy/leiningen/$LEIN_VERSION/bin/lein-
pkg \  
&& echo "Comparing lein-pkg checksum ..." \  
&& echo "$LEIN_DOWNLOAD_SHA *lein-pkg" | sha1sum -c - \  
&& mv lein-pkg $LEIN_INSTALL/lein \  
&& chmod 0755 $LEIN_INSTALL/lein \  
&& wget -q
https://github.com/technomancy/leiningen/releases/download/$LEIN_VERSION/leiningen-$LEIN_VERSION-
standalone.zip \  
&& wget -q
https://github.com/technomancy/leiningen/releases/download/$LEIN_VERSION/leiningen-$LEIN_VERSION-
standalone.zip.asc \  
&& gpg --keyserver pool.sks-keyservers.net --recv-key
2B72BF956E23DE5E830D50F6002AF007D1A7CC18 \  
&& echo "Verifying Jar file signature ..." \  
&& gpg --verify leiningen-$LEIN_VERSION-standalone.zip.asc \  
&& rm leiningen-$LEIN_VERSION-standalone.zip.asc \  
&& mkdir -p /usr/share/java \  
&& mv leiningen-$LEIN_VERSION-standalone.zip
/usr/share/java/leiningen-$LEIN_VERSION-standalone.jar  
  
ENV PATH=$PATH:$LEIN_INSTALL  
ENV LEIN_ROOT 1  
# Install clojure 1.9.0-RC2 so users don't have to download it every time  
RUN echo '(defproject dummy "" :dependencies [[org.clojure/clojure
"1.9.0-RC2"]])' > project.clj \  
&& lein deps && rm project.clj  
  
###############################################################################  
# Ruby/Bundler  
#  
# Ref: http://bit.ly/2AVMEQp  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
# SHA from http://bit.ly/2koIl5u  
ENV RUBY_MAJOR=2.4  
ENV RUBY_VERSION=2.4.2  
ENV
RUBY_DOWNLOAD_SHA256=93b9e75e00b262bc4def6b26b7ae8717efc252c47154abb7392e54357e6c8c9c  
  
# Rubygems version determined from https://rubygems.org/pages/download  
ENV RUBYGEMS_VERSION 2.7.3  
RUN set -ex \  
\  
&& buildDeps=' \  
bison \  
libgdbm-dev \  
ruby \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O ruby.tar.gz "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
\  
&& mkdir -p /usr/src/ruby \  
&& tar xvfz ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
\  
&& cd /usr/src/ruby \  
&& { \  
echo '#define ENABLE_PATH_CHECK 0'; \  
echo; \  
cat file.c; \  
} > file.c.new \  
&& mv file.c.new file.c \  
\  
&& autoconf \  
&& ./configure --disable-install-doc --enable-shared \  
&& make -j"$(nproc)" \  
&& make install \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
&& cd / \  
&& rm -r /usr/src/ruby \  
\  
&& gem update --system "$RUBYGEMS_VERSION"  
  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
###############################################################################  
# Terraform  
#  
# Ref: http://bit.ly/2zQjheb - checksums available here http://bit.ly/2DoWVTF  
ENV TERRAFORM_VERSION=0.11.3  
ENV
TERRAFORM_SHA256SUM=6b8a7b83954597d36bbed23913dd51bc253906c612a070a21db373eab71b277b  
  
RUN apt-get update && apt-get install -y unzip && \  
curl
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
> terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
echo "${TERRAFORM_SHA256SUM} terraform_${TERRAFORM_VERSION}_linux_amd64.zip" >
terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
sha256sum -c terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \  
rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
  
###############################################################################  
# AWS CLI  
#  
RUN apt-get install -y python-pip && \  
pip install awscli  
  
###############################################################################  
# MySQL Client  
#  
RUN apt-get install -y mysql-client  
  
###############################################################################  
# Other bits and pieces  
#  
RUN apt-get install -y jq  
  
CMD [ "irb" ]  

