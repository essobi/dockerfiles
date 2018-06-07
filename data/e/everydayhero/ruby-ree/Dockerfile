FROM kneip/ree-1.8.7-2012.02  
RUN apt-get update && apt-get install -y \  
curl \  
wget \  
git \  
autoconf \  
build-essential \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
xfonts-75dpi \  
xvfb \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb \  
&& dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb \  
&& rm wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
  
# skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
# install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
# don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
CMD ["irb"]  

