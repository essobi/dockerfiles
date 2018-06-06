FROM debian:jessie  
  
MAINTAINER Dan Slinky <dan@danslinky.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#WORKDIR /data  
# Install base packages.  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends -y wget vim curl sysstat git curl \  
procps autoconf build-essential libbz2-dev libcurl4-openssl-dev libffi-dev \  
libssl-dev libreadline-dev libyaml-dev zlib1g-dev libpq-dev libsasl2-dev  
  
# Install, recompile and reinstall Ruby...  
ENV RUBY_MAJOR 2.4  
ENV RUBY_VERSION 2.4.0  
RUN apt-get update \  
&& apt-get install -y bison ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" | tar -xjC
/usr/src/ruby --strip-components=1 \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& apt-get purge -y --auto-remove bison ruby \  
&& make install \  
&& rm -r /usr/src/ruby  
  
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
  
# Install Puppet.  
#RUN \  
# wget --quiet https://apt.puppetlabs.com/puppetlabs-release-jessie.deb && \  
# dpkg -i puppetlabs-release-jessie.deb && \  
# apt-get update && \  
# apt-get install --no-install-recommends -y puppet git && \  
# gem install yaml-lint puppet-lint rspec-puppet librarian-puppet r10k --no-ri
--no-rdoc && \  
# rm -f puppetlabs-release-jessie.deb  
# Install Sensu repo and binaries.  
RUN \  
wget -q http://repositories.sensuapp.org/apt/pubkey.gpg -O- | apt-key add - &&
\  
echo "deb http://repositories.sensuapp.org/apt sensu main" >
/etc/apt/sources.list.d/sensu.list && \  
apt-get update && \  
apt-get install --no-install-recommends -y sensu  
  
# Install a load of sensu plugins  
RUN \  
gem install --no-ri --no-rdoc \  
sensu-plugins-http \  
sensu-plugins-rabbitmq \  
sensu-plugins-load-checks \  
sensu-plugins-postgres \  
sensu-plugins-slack \  
sensu-plugins-sensu \  
sensu-plugins-dns \  
sensu-plugins-ssl \  
sensu-plugins-zookeeper \  
sensu-plugins-elasticsearch \  
sensu-plugins-kubernetes \  
sensu-plugins-pagerduty \  
sensu-plugins-aws \  
sensu-plugins-jenkins \  
sensu-plugins-redis \  
sensu-plugins-fluentd  
  
COPY slack.rb /usr/local/bundle/bin/slack.rb  
  
# Clean up image.  
RUN \  
apt-get autoremove -y && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc /usr/share/man /usr/share/locale  
  

