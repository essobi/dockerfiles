FROM ubuntu:xenial  
  
MAINTAINER David Gillies <dave.gillies@gmail.com>  
ENV DISTRIBUTION ubuntu  
ENV RELEASE xenial  
ENV REFRESHED_AT 2017-12-05  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq -y && apt-get install -q -y --no-install-recommends \  
build-essential curl git ruby bundler ruby-dev lsb-release ca-certificates
dash unzip openssh-client jq; \  
apt-get dist-upgrade -q -y --force-yes; \  
apt-get clean ; \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
COPY Gemfile .  
RUN echo "gem: --no-ri --no-rdoc" >/etc/gemrc; \  
bundle install --without deployment --binstubs /usr/local/bin  
  
COPY run.sh /usr/local/bin/  
  
VOLUME /data  
WORKDIR /data  
  
CMD ["run.sh", "recipe.rb"]  

