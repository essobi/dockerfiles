FROM shift/ubuntu:15.04  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
ENV RUBY_VERSION 2.1.5  
ENV HOME /root  
  
RUN apt-get update \  
&& apt-get install build-essential curl git ruby ruby-dev libpq5 libpq-dev
nodejs libreadline-dev \--yes \--force-yes \  
&& echo 'gem: \--no-rdoc \--no-ri' >> ~/.gemrc \  
&& gem install bundler \  
&& useradd -ms /bin/bash deploy \  
&& git clone git://github.com/sstephenson/rbenv.git /home/deploy/.rbenv \  
&& echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> /home/deploy/.bashrc \  
&& echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> /root/.bashrc \  
&& echo 'eval "$(rbenv init -)"' >> /home/deploy/.bashrc \  
&& git clone git://github.com/sstephenson/ruby-build.git
/home/deploy/.rbenv/plugins/ruby-build \  
&& echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >>
/home/deploy/.bashrc \  
&& echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >>
/root/.bashrc \  
&& git clone https://github.com/sstephenson/rbenv-gem-rehash.git
/home/deploy/.rbenv/plugins/rbenv-gem-rehash \  
&& git clone https://github.com/ianheggie/rbenv-binstubs.git
/home/deploy/.rbenv/plugins/rbenv-binstubs \  
&& curl -f -L -o /usr/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 \  
&& chmod 0755 /usr/bin/confd \  
&& echo 'gem: \--no-rdoc \--no-ri' >> /home/deploy/.gemrc \  
&& rm -rf /var/lib/apt/lists/* \  
&& chown -R deploy:deploy /home/deploy  
  
USER deploy  
WORKDIR /home/deploy  
ENV HOME /home/deploy  
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/plugins/ruby-
build/bin:$HOME/.rbenv/shims:$PATH  
RUN bash -l -c 'eval "$(rbenv init -)" \  
&& rbenv install $RUBY_VERSION \  
&& rbenv local $RUBY_VERSION \  
&& gem install bundler'  
  
ENV HOME /home/deploy  
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/plugins/ruby-
build/bin:$HOME/.rbenv/shims:$PATH  
ENV RAILS_ENV docker  
  
WORKDIR /home/deploy/app  
ONBUILD ADD . /home/deploy/app  
ONBUILD USER root  
ONBUILD RUN chown deploy:deploy -R /home/deploy  
ONBUILD USER deploy  
ONBUILD RUN bash -l -c 'eval "$(rbenv init -)" \  
&& bundle install \--binstubs .bundle/bin \--deployment \--jobs 5 \--without
development test \  
&& bundle check \  
&& bundle exec rake tmp:create \  
&& mkdir log \  
&& bundle env'  
  

