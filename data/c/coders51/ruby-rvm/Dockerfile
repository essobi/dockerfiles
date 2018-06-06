FROM ubuntu:14.04  
MAINTAINER coders51 <dev@coders51.com>  
  
LABEL Description="ruby 2.0.0-p247 with debugger 1.6.6 and rails 4.0.1 from
RVM"  
  
RUN apt-get update && apt-get install -y \  
curl \  
libxml2-dev \  
libxslt-dev \  
libcurl4-openssl-dev \  
libreadline6-dev \  
libssl-dev \  
patch \  
build-essential \  
zlib1g-dev \  
openssh-server \  
libyaml-dev \  
libicu-dev \  
libmysqlclient-dev \  
gawk \  
libsqlite3-dev \  
sqlite3 \  
autoconf \  
libgmp-dev \  
libgdbm-dev \  
libncurses5-dev \  
automake \  
libtool \  
bison \  
libffi-dev \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable  
RUN /usr/local/rvm/bin/rvm install 2.0.0-p247  
RUN /usr/local/rvm/bin/rvm alias create default 2.0.0-p247  
RUN /usr/local/rvm/bin/rvm system 2.0.0-p247  
  
ENV PATH=${PATH}:/usr/local/rvm/wrappers/ruby-2.0.0-p247  
  
RUN gem install bundler sass  
RUN gem install debugger -v 1.6.6  
RUN gem install rails -v 4.0.1  
RUN gem install unicorn -v 4.6.3  
RUN gem install tire -v 0.6.2  
RUN gem install sshkit -v 1.5.1  
RUN gem install sprockets -v 2.11.0  
RUN gem install sprockets-rails -v 2.0.1  
RUN gem install sidekiq -v 3.2.6  
RUN gem install sass-rails -v 4.0.3  
RUN gem install sass -v 3.2.19  
RUN gem install rspec -v 3.0.0.beta2  
RUN gem install rspec-rails -v 3.0.0.beta2  
  

