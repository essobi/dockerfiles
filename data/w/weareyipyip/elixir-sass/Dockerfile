FROM ruby:2.1  
LABEL maintainer "YipYip <devops@yipyip.nl>"  
  
ENV ELIXIR_VERSION="v1.6.2"  
ENV
ELIXIR_DOWNLOAD_SHA256="64779258e60ddf220fde75c9d972c00ff7760cbd0edbe555c93e3f892f8b0726"  
ENV LANG=C.UTF-8  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb &&
dpkg -i erlang-solutions_1.0_all.deb  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update && apt-get install -y nodejs build-essential inotify-tools
esl-erlang curl ca-certificates unzip && npm install npm -g  
RUN npm install -g \  
brunch \  
node-gyp  
  
RUN set -xe \  
&& ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/archive/${ELIXIR_VERSION}.tar.gz" \  
&& ELIXIR_DOWNLOAD_SHA256="${ELIXIR_DOWNLOAD_SHA256}" \  
&& curl -fSL -o elixir-src.tar.gz $ELIXIR_DOWNLOAD_URL \  
&& echo "$ELIXIR_DOWNLOAD_SHA256 elixir-src.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/local/src/elixir \  
&& tar -xzC /usr/local/src/elixir --strip-components=1 -f elixir-src.tar.gz \  
&& rm elixir-src.tar.gz \  
&& cd /usr/local/src/elixir \  
&& make install clean  
  
RUN gem install sass -v 3.5.4  
RUN gem install compass  
  
CMD ["iex"]

