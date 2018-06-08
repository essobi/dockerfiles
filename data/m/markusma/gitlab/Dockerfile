# gitlab with nginx, etcd registration, confd and supervisord on Ubuntu Trusty  
FROM markusma/nginx-etcdregister:1.7  
MAINTAINER Markus Mattinen <markus@gamma.fi>  
  
RUN addgroup --gid 999 git \  
&& adduser --disabled-login --uid 999 --gid 999 git \  
&& mkdir -p /var/run/sshd  
  
RUN curl -sSL http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key
add - \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list \  
&& add-apt-repository ppa:chris-lea/redis-server \  
&& add-apt-repository ppa:git-core/ppa \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends build-essential zlib1g-dev
libyaml-dev libssl-dev libgdbm-dev libreadline-dev libncurses5-dev libffi-dev
openssh-server redis-server checkinstall libxml2-dev libxslt-dev
libcurl4-openssl-dev \  
libicu-dev python python-docutils msmtp-mta sudo openjdk-7-jre-headless git
postgresql-9.3 libpq-dev pkg-config cmake \  
&& mkdir -p /tmp/ruby \  
&& cd /tmp/ruby \  
&& curl -sSL ftp://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz | tar xz \  
&& cd ruby-2.1.2 \  
&& ./configure --disable-install-rdoc \  
&& make -j4 \  
&& make install \  
&& cd / \  
&& rm -rf /tmp/ruby \  
&& cd /home/git \  
&& su git -c "git clone https://github.com/gitlabhq/gitlab-shell.git -b
v2.0.1" \  
&& su git -c "git clone https://github.com/gitlabhq/gitlabhq.git -b 7-5-stable
gitlab" \  
&& cd /home/git/gitlab \  
&& usermod -aG redis git \  
&& su git -c "cp /home/git/gitlab-shell/config.yml.example /home/git/gitlab-
shell/config.yml" \  
&& su git -c "cp config/initializers/rack_attack.rb.example
config/initializers/rack_attack.rb" \  
&& su git -c "cp config/resque.yml.example config/resque.yml" \  
&& gem install bundler --no-ri --no-rdoc \  
&& su git -c "bundle install -j`nproc` --deployment --without development test
mysql aws" \  
&& apt-get purge -y build-essential checkinstall python-docutils \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN su git -c "HOME=/home/git git config --global user.name 'GitLab'" \  
&& su git -c "HOME=/home/git git config --global user.email
'gitlab@localhost'" \  
&& su git -c "HOME=/home/git git config --global core.autocrlf input" \  
&& mkdir -p /home/git/gitlab-satellites /home/git/gitlab/tmp/pids
/home/git/gitlab/tmp/sockets /home/git/gitlab/public/uploads  
  
ADD config/home/git /home/git  
  
RUN chown -R git:git /home/git  
  
ADD config/etc/redis.conf /etc/redis.conf  
ADD config/etc/supervisor/conf.d /etc/supervisor/conf.d  
ADD config/init /init  
ADD config/check /check  
ADD config/start_unicorn /start_unicorn  
ADD config/start_sidekiq /start_sidekiq  
ADD config/etc/confd/conf.d /etc/confd/conf.d  
ADD config/etc/confd/templates /etc/confd/templates  
  
EXPOSE 5000 22  
VOLUME [ "/home/git/.ssh", "/home/git/repositories", "/home/git/gitlab-
satellites", "/var/lib/redis", "/etc/ssh" ]  

