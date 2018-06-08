FROM node:0.10.35  
RUN apt-get update -yq  
RUN apt-get install postgresql-client -yqq  
RUN apt-get install -y curl patch gawk g++ gcc make libc6-dev patch
libreadline6-dev zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3
autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-
dev  
  
RUN mkdir /rvm  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable"  
RUN /bin/bash -l -c "rvm install 2.0"  
RUN /bin/bash -l -c "echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
  
ADD ./entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

