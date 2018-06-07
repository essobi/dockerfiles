FROM hachque/systemd-none  
  
# Update base image  
RUN zypper --non-interactive patch || true  
# Update again in case package manager was updated.  
RUN zypper --non-interactive patch  
  
# Add user  
RUN echo "diaspora:x:4096:4096:user for diaspora:/srv/diaspora:/bin/bash" >>
/etc/passwd  
RUN echo "diaspora:!:4096:" >> /etc/group  
  
# Install requirements for clone  
RUN zypper --non-interactive in git  
  
# Create storage location for diaspora  
RUN mkdir /srv/diaspora  
RUN chown diaspora:diaspora /srv/diaspora  
RUN cd /srv/diaspora  
  
# Clone Diaspora  
RUN chown -Rv diaspora:diaspora /srv/diaspora  
RUN chmod -Rv u+rwX /srv/diaspora  
RUN su diaspora -c "git clone -b master git://github.com/diaspora/diaspora.git
/srv/diaspora/diaspora"  
  
# Install requirements  
#RUN zypper --non-interactive in ruby-devel rubygem-bundler make automake gcc
gcc-c++ libcurl-devel ImageMagick ImageMagick-extra libtool bison libtool
patch libxml2-devel libxslt-devel libffi-devel libyaml-devel nodejs redis curl
git ca-certificates ca-certificates-mozilla ca-certificates-cacert which gdbm-
devel libopenssl-devel libdb-4_5 sqlite3-devel libmysqlclient-devel  
RUN zypper --non-interactive in ruby-devel rubygem-bundler make automake gcc
gcc-c++ libcurl-devel ImageMagick ImageMagick-extra libtool bison libtool
patch libxml2-devel libxslt-devel libffi-devel libyaml-devel nodejs nginx
rubygem-passenger-nginx redis curl git ca-certificates ca-certificates-mozilla
ca-certificates-cacert which gdbm-devel libopenssl-devel libdb-4_5
sqlite3-devel libmysqlclient-devel  
RUN zypper --non-interactive rm ruby ruby-common ruby-devel ruby20-devel
rubygem-bundler rubygem-passenger rubygem-passenger-nginx rubygem-rack  
  
# Setup REDIS  
RUN cp /etc/redis/default.conf.example /etc/redis/default.conf  
RUN chown redis: /etc/redis/default.conf  
  
# Trust GPG signatures  
RUN su diaspora -c 'gpg2 --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3'  
  
# Setup RVM  
RUN su diaspora -c 'curl -L dspr.tk/1t | bash'  
RUN su diaspora -c 'source "$HOME/.rvm/scripts/rvm" && rvm autolibs read-fail'  
RUN su diaspora -c 'source "$HOME/.rvm/scripts/rvm" && rvm install 2.1.5'  
  
# Install Ruby libraries  
RUN su diaspora -c 'source "$HOME/.rvm/scripts/rvm" && cd
/srv/diaspora/diaspora && gem install bundler'  
RUN su diaspora -c 'source "$HOME/.rvm/scripts/rvm" && cd
/srv/diaspora/diaspora && RAILS_ENV=production DB=mysql bin/bundle install
--without test development'  
RUN su diaspora -c 'source "$HOME/.rvm/scripts/rvm" && cd
/srv/diaspora/diaspora && RAILS_ENV=production DB=mysql gem install passenger
-v "5.0.13"'  
  
# Install NGINX with Passenger  
RUN zypper --non-interactive in sudo  
RUN su diaspora -c 'source "$HOME/.rvm/scripts/rvm" && cd
/srv/diaspora/diaspora && passenger-install-nginx-module --auto
--prefix=/srv/diaspora/nginx'  
  
# Add rvm include to bashrc  
RUN su diaspora -c 'echo "source \"\$HOME/.rvm/scripts/rvm\"" >>
/srv/diaspora/.bashrc'  
  
# Install Ghostscript fonts  
RUN zypper --non-interactive in ghostscript-fonts-std ghostscript-fonts-other  
  
# Expose port 80 and 443  
EXPOSE 80  
EXPOSE 443  
# Add files  
ADD 10-boot-conf /etc/init.simple/10-boot-conf  
ADD 20-redis /etc/init.simple/20-redis  
ADD 25-nginx /etc/init.simple/25-nginx  
ADD 30-server /etc/init.simple/30-server

