FROM ubuntu:12.10  
MAINTAINER Marcin Kulik  
  
ENV RAILS_ENV production  
  
# disable startup of services during image creation  
RUN echo exit 101 > /usr/sbin/policy-rc.d && chmod +x /usr/sbin/policy-rc.d  
  
# enable ssh root access via keys stored in host's config/authorized_keys  
RUN mkdir /root/.ssh && ln -s /var/lib/gitorious/config/authorized_keys
/root/.ssh/authorized_keys  
RUN mkdir /var/run/sshd  
  
# add git user with empty authorized_keys file  
RUN adduser git  
RUN mkdir -p /home/git/.ssh && touch /home/git/.ssh/authorized_keys; \  
chown -R git:git /home/git/.ssh; \  
chmod 0700 /home/git/.ssh && chmod 0600 /home/git/.ssh/authorized_keys  
  
# install required packages  
RUN apt-get -y update  
RUN apt-get -y install build-essential curl git redis-server \  
git-daemon-sysvinit nginx supervisor sphinxsearch \  
openssh-server mysql-client mysql-server libmysqlclient-dev \  
ruby ruby-dev rake libxml2-dev libxslt1-dev \  
libreadline6 libicu-dev memcached imagemagick postfix  
  
# install bundler  
RUN gem install bundler --no-rdoc --no-ri  
  
# install Gitorious vhost and make nginx not daemonize  
RUN ln -fs /srv/gitorious/docker/config/nginx/nginx.conf
/etc/nginx/nginx.conf; \  
ln -fs /srv/gitorious/docker/config/nginx/gitorious.conf /etc/nginx/sites-
enabled/default  
  
# setup MySQL  
RUN mysql_install_db  
RUN mv /var/lib/mysql /var/lib/mysql-template  
RUN ln -s /var/lib/gitorious/data/mysql /var/lib/mysql  
RUN rm /etc/mysql/my.cnf && ln -s /srv/gitorious/docker/config/my.cnf
/etc/mysql/my.cnf  
  
# create dir for the app and docker's files  
RUN mkdir -p /srv/gitorious && chown git:git /srv/gitorious  
  
# checkout and build the app in /srv/gitorious/app  
RUN su git -c "git clone git://gitorious.org/gitorious/mainline.git
/srv/gitorious/app; \  
cd /srv/gitorious/app; \  
git checkout 445384d; \  
git submodule update --recursive --init; \  
bundle install --deployment --without development test postgres && \  
bundle exec rake assets:precompile"  
# symlink internal config files  
RUN ln -s /srv/gitorious/docker/config/unicorn.rb /srv/gitorious/app/config/;
\  
ln -s /srv/gitorious/docker/config/memcache.yml /srv/gitorious/app/config/; \  
ln -s /srv/gitorious/docker/config/gitorious.overrides.yml
/srv/gitorious/app/config/  
  
# symlink external (exposed) config files  
RUN ln -s /var/lib/gitorious/config/database.yml /srv/gitorious/app/config/; \  
ln -s /var/lib/gitorious/config/gitorious.yml /srv/gitorious/app/config/; \  
ln -s /var/lib/gitorious/config/smtp.yml /srv/gitorious/app/config/; \  
ln -s /var/lib/gitorious/config/authentication.yml /srv/gitorious/app/config/  
# expose log files  
RUN rm -rf /srv/gitorious/app/log && ln -s /var/lib/gitorious/data/logs
/srv/gitorious/app/log  
# setup /usr/bin/gitorious so it executes bin/gitorious in the app dir  
RUN echo "#!/bin/sh\n\nexec /srv/gitorious/app/bin/gitorious \"\$@\"" >
/usr/bin/gitorious && chmod a+x /usr/bin/gitorious  
# symlink supervisord config file  
RUN rm /etc/supervisor/supervisord.conf && ln -s
/srv/gitorious/docker/config/supervisord.conf /etc/supervisor/supervisord.conf  
  
# copy all files from gitorious-docker repo to the image  
ADD . /srv/gitorious/docker  
  
# expose directory with data and config files to the host  
VOLUME ["/var/lib/gitorious"]  
  
EXPOSE 80  
EXPOSE 22  
EXPOSE 9418  
  
ENTRYPOINT ["/srv/gitorious/docker/bin/run"]  
CMD ["supervisord", "-n"]  

