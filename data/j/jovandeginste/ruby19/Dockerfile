FROM ubuntu  
MAINTAINER Jo Vandeginste "jo.vandeginste@gmail.com"  
  
RUN apt-get update \  
&& apt-get install -y git-core curl libmysqlclient-dev build-essential openssl
libreadline6 libreadline6-dev curl zlib1g zlib1g-dev libssl-dev libyaml-dev
libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev
automake libtool bison pkg-config \  
&& update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX \  
&& rm -rf /var/lib/apt/lists/* # 20140918  
  
# install RVM, Ruby, and Bundler  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \  
&& curl -L https://get.rvm.io | bash -s stable \  
&& /bin/bash -l -c "rvm requirements" \  
&& /bin/bash -l -c "rvm install 1.9" \  
&& /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  

