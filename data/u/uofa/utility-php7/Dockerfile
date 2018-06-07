FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Configured timezone.  
ENV TZ=Australia/Adelaide  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Ensure UTF-8.  
ENV LANG en_AU.UTF-8  
ENV LC_ALL en_AU.UTF-8  
# Use nearby apt mirror.  
#RUN sed -i
's%http://archive.ubuntu.com/ubuntu/%mirror://mirrors.ubuntu.com/mirrors.txt%'
/etc/apt/sources.list  
# Install the universe.  
RUN apt-get update \  
&& apt-get -y install locales \  
&& locale-gen en_AU.UTF-8 \  
&& apt-get -y install apt-transport-https ca-certificates wget \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >
/etc/apt/sources.list.d/docker.list \  
&& echo 'deb https://dl.yarnpkg.com/debian/ stable main' >
/etc/apt/sources.list.d/yarn.list \  
&& wget -q --show-progress -O - https://dl.yarnpkg.com/debian/pubkey.gpg |
apt-key add - \  
&& wget -q --show-progress -O - https://deb.nodesource.com/setup_6.x | bash -
\  
&& apt-get update \  
&& apt-get -y dist-upgrade \  
&& apt-get -y install docker-engine \  
&& apt-get -y install php7.0 php7.0-cli php7.0-common php-memcached php-xdebug
php7.0-bcmath php7.0-curl php7.0-gd php7.0-ldap php7.0-mbstring php7.0-mysql
php7.0-opcache php7.0-xml php7.0-zip libedit-dev tig vim curl ssh git-flow
silversearcher-ag mysql-client netcat-openbsd pv ruby-dev rubygems-integration
nodejs yarn build-essential sudo zip ssmtp python \  
&& apt-get -y autoremove \  
&& apt-get autoclean \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Bundler.  
RUN gem install bundler  
  
# Install Robo.  
RUN wget -q --show-progress -O /usr/local/bin/robo
https://github.com/consolidation/Robo/releases/download/1.2.2/robo.phar &&
chmod +x /usr/local/bin/robo  
  
# Install Drush.  
RUN wget -q --show-progress -O /usr/local/bin/drush https://github.com/drush-
ops/drush/releases/download/8.1.16/drush.phar && chmod +x /usr/local/bin/drush  
  
# Install Drupal console.  
RUN wget -q --show-progress -O /usr/local/bin/drupal
https://drupalconsole.com/installer && chmod +x /usr/local/bin/drupal  
  
# Install Composer.  
RUN wget -q --show-progress -q https://getcomposer.org/installer -O - | php --
--install-dir=/usr/local/bin --filename=composer  
  
# Add smtp support.  
RUN echo "sendmail_path = /usr/sbin/ssmtp -t" > /etc/php/7.0/mods-
available/sendmail.ini \  
&& echo "mailhub=mail:25\nUseTLS=NO\nFromLineOverride=YES" >
/etc/ssmtp/ssmtp.conf \  
&& phpenmod -v ALL -s ALL sendmail  
  
# Enable sshd.  
RUN mkdir -p /var/run/sshd && chmod -775 /var/run/sshd  
  
COPY ./files/bash_aliases /root/.bash_aliases  
COPY ./files/gitconfig /root/.gitconfig  
COPY ./files/profile /root/.profile  
COPY ./files/xdebug_setup.sh /usr/local/bin/xdebug_setup.sh  
COPY ./files/entry.sh /entry.sh  
  
# Setup a directory ready for the user which is dynamically created.  
RUN mkdir -p /code  
  
COPY ./files/bash_aliases /code/.bash_aliases  
COPY ./files/gitconfig /code/.gitconfig  
COPY ./files/profile /code/.profile  
  
# Expose ports.  
EXPOSE 22  
WORKDIR /code  
  
CMD ["/usr/sbin/sshd", "-D"]  

