FROM ubuntu:trusty  
  
RUN apt-get install -y \  
git-core \  
curl \  
zlib1g-dev \  
build-essential \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
libxml2-dev \  
libxslt1-dev  
  
  
ENV RBENV_ROOT /usr/local/rbenv  
ENV PATH
/usr/local/rbenv/shims:/usr/local/rbenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games  
  
RUN curl https://raw.githubusercontent.com/fesplugas/rbenv-
installer/master/bin/rbenv-installer | bash  
  
ADD default-gems /usr/local/rbenv/default-gems  
  
RUN curl -fsSL https://gist.github.com/mislav/a18b9d7f0dc5b9efc162.txt | rbenv
install --patch 2.1.1 rbenv global 2.1.1  
RUN rbenv global 2.1.1  
  
ADD rbenv.sh /etc/profile.d/rbenv.sh  
RUN chmod a+x /etc/profile.d/rbenv.sh  

