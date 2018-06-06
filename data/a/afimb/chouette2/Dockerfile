FROM centos:6.6  
MAINTAINER Cityway  
  
ENV GIT_BRANCH V3_3  
ENV RUBY_VERSION 2.3.3  
LABEL Description="Chouette GUI" \  
Usage="docker run -it --name chouette2 --link chouette-postgres:chouette-
postgres --link smtp:smtp --link chouette-iev:chouette-iev -p 3000:3000 -d
chouette2" \  
BuildUsage="docker build -t chouette2 ." \  
License="CECILL/B" \  
Version="3.0"  
  
RUN yum -y install yum-plugin-ovl  
RUN yum -y install epel-release && yum -y update  
RUN yum -y localinstall
https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-6-x86_64/pgdg-
centos94-9.4-2.noarch.rpm  
RUN yum -y install which tar git postgresql94-devel proj proj-devel geos-devel
nmap bzip2 zlib zlib-devel gcc-c++ patch readline readline-devel libyaml-devel
libffi-devel openssl-devel make autoconf automake libtool bison curl sqlite-
devel  
  
#-- Add user chouette  
RUN adduser chouette  
  
USER chouette  
  
RUN mkdir ~/chouette-gui && \  
git clone https://github.com/rbenv/rbenv.git ~/.rbenv && \  
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile && \  
echo 'eval "$(rbenv init -)"' >> ~/.bash_profile && \  
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
&& \  
source ~/.bash_profile && \  
type rbenv && \  
rbenv install $RUBY_VERSION && rbenv global $RUBY_VERSION && \  
gem install bundler && bundle config build.pg --with-pg-
config=/usr/pgsql-9.4/bin/pg_config && \  
git clone -b $GIT_BRANCH git://github.com/afimb/chouette2 ~/chouette-gui/ && \  
cd ~/chouette-gui && bundle install && \  
mkdir /home/chouette/bin  
  
#-- Configure Chouette2  
COPY config/chouette.sh /home/chouette/bin  
COPY config/chouette.conf /home/chouette/bin  
COPY config/application.yml /home/chouette/chouette-gui/config/  
COPY config/smtp_settings.rb /home/chouette/chouette-gui/config/initializers/  
COPY config/database.yml /home/chouette/chouette-gui/config  
  
EXPOSE 3000  
COPY config/docker-entrypoint.sh /  
VOLUME ["/home/chouette/referentials"]  
ENTRYPOINT ["/docker-entrypoint.sh"]

