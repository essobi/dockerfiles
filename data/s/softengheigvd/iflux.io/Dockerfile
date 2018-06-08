FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
RUN npm install -g grunt-cli  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.5  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
build-essential \  
ca-certificates \  
curl \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
pkg-config \  
procps \  
python \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/ruby \  
&& curl -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \  
| tar -xjC /usr/src/ruby --strip-components=1 \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& rm -r /usr/src/ruby  
  
# skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
# install things globally  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
RUN gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin" \  
&& gem install \  
jekyll \  
github-pages \  
jekyll-redirect-from \  
kramdown  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD _apidoc/apidoc-seed/package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /jekyll/iflux-blog/_apidoc/apidoc-seed && cp -a /tmp/node_modules
/jekyll/iflux-blog/_apidoc/apidoc-seed  
  
ADD . /jekyll/iflux-blog  
  
RUN cd /jekyll/iflux-blog/_apidoc/apidoc-seed \  
&& grunt prod --baseUrl="{{ site.baseurl }}/api" \--apiUrl="{{ site.apiUrl }}"
\--ifluxUrl="{{ site.ifluxUrl }}" \--blogUrl="{{ site.baseurl }}" \  
&& mkdir -p /jekyll/iflux-blog/api \  
&& rm -rf /jekyll/iflux-blog/api/* \  
&& mv /jekyll/iflux-blog/_apidoc/apidoc-seed/build/* /jekyll/iflux-blog/api \  
&& rm -rf /jekyll/iflux-blog/_apidoc \  
&& rm /jekyll/iflux-blog/_config.yml \  
&& rm /jekyll/iflux-blog/_config_local.yml \  
&& mv /jekyll/iflux-blog/_config_docker.yml /jekyll/iflux-blog/_config.yml  
  
RUN useradd -m -r -U iflux \  
&& chown -R iflux:iflux /jekyll/iflux-blog  
  
USER iflux  
  
WORKDIR /jekyll/iflux-blog  
  
EXPOSE 4000  
CMD ["jekyll", "serve", "--host=0.0.0.0"]  

