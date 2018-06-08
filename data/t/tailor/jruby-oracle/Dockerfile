FROM tailor/java-oracle:latest  
MAINTAINER Nadav Shatz <nadav@tailorbrands.com>  
  
RUN add-apt-repository -y ppa:webupd8team/java  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg
main" > /etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
RUN apt-get update && apt-get install -y git-core wget build-essential
zlib1g-dev \  
libssl-dev libreadline6-dev libyaml-dev libgdbm-dev libffi-dev \  
libxml2-dev libxslt1-dev libncurses5-dev libfuse2 tcl-dev \  
libpng-dev libjpeg-dev libgs-dev libbz2-dev libfreetype6-dev \  
libtiff-dev librsvg2-dev libpq-dev postgresql-client-9.5 \  
curl apt-transport-https libc6-dev --no-install-recommends  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV JRUBY_VERSION 9.1.15.0  
ENV JRUBY_SHA256
4a0d9305867ed327a8cf4f7ff8a65c7ff62094a495ec85463d0792656762469e  
RUN mkdir /opt/jruby \  
&& curl -fSL
https://s3.amazonaws.com/jruby.org/downloads/${JRUBY_VERSION}/jruby-
bin-${JRUBY_VERSION}.tar.gz -o /tmp/jruby.tar.gz \  
&& echo "$JRUBY_SHA256 /tmp/jruby.tar.gz" | sha256sum -c - \  
&& tar -zx --strip-components=1 -f /tmp/jruby.tar.gz -C /opt/jruby \  
&& rm /tmp/jruby.tar.gz \  
&& update-alternatives --install /usr/local/bin/ruby ruby /opt/jruby/bin/jruby
1  
ENV PATH /opt/jruby/bin:$PATH  
  
# skip installing gem documentation  
RUN mkdir -p /opt/jruby/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /opt/jruby/etc/gemrc  
  
RUN gem install bundler  
  
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
  
# Node.js  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs yarn  
  
# Image magick  
ENV IMAGE_MAGICK_VER 7.0.7-17  
RUN wget https://s3.amazonaws.com/tailorbrands-
ops/ImageMagick-${IMAGE_MAGICK_VER}.tar.gz && \  
tar xvzf ImageMagick-${IMAGE_MAGICK_VER}.tar.gz && \  
cd ImageMagick-${IMAGE_MAGICK_VER} && \  
./configure --with-gslib=yes --with-rsvg=yes && \  
make && \  
make install && \  
ldconfig /usr/local/lib  
  
# Potrace  
ENV POTRACE_VER 1.13  
RUN wget https://s3.amazonaws.com/tailorbrands-
ops/potrace-${POTRACE_VER}.tar.gz && \  
tar xzvf potrace-${POTRACE_VER}.tar.gz && \  
cd potrace-${POTRACE_VER} && \  
./configure && \  
make && \  
make install  
  
RUN apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
CMD [ "/bin/bash" ]  

