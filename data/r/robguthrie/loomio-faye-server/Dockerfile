# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/passenger-ruby21:0.9.18  
MAINTAINER Robert Guthrie <rob@loomio.org>  
  
# Set correct environment variables.  
ENV HOME /root  
  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# build ruby  
run apt-get update  
run apt-get install -y software-properties-common \  
git-core curl build-essential spamassassin spamc \  
autoconf bison build-essential libssl-dev libyaml-dev \  
libreadline6 libreadline6-dev zlib1g zlib1g-dev libssl-doc \  
authbind python  
  
USER app  
ENV HOME /home/app  
  
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
  
# switch to root to install ruby build then switch back to app  
USER root  
RUN ~/.rbenv/plugins/ruby-build/install.sh  
  
USER app  
ENV PATH ~/.rbenv/bin:~/.rbenv/shims:$PATH  
RUN ~/.rbenv/bin/rbenv install 2.2.3  
RUN ~/.rbenv/bin/rbenv global 2.2.3  
RUN ~/.rbenv/bin/rbenv rehash  
RUN ~/.rbenv/shims/gem update --system  
RUN ~/.rbenv/shims/gem install bundler  
RUN ~/.rbenv/bin/rbenv rehash  
  
# copy app from CWD to /home/app  
COPY Gemfile.lock Gemfile private_pub.ru /home/app/  
  
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/shims:$PATH  
  
WORKDIR /home/app  
RUN ~/.rbenv/shims/bundle  
  
CMD thin --port 4443 \  
\--ssl \  
\--ssl-key-file /home/app/cert/$SSL_KEY_FILE \  
\--ssl-cert-file /home/app/cert/$SSL_CERT_FILE \  
\--ssl-disable-verify \  
\--environment production \  
\--rackup private_pub.ru \  
start  

