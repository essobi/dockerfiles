FROM million12/php-testing:php56  
MAINTAINER Jonas Renggli <jonas.renggli@swisscom.com>  
  
# - Install OpenSSH server  
# - Generate required host keys  
# - Remove 'Defaults secure_path' from /etc/sudoers which overrides path when
using 'sudo' command  
# - Add 'www' user to sudoers  
# - Remove non-necessary Supervisord services from parent image
'million12/nginx-php'  
# - Remove warning about missing locale while logging in via ssh  
RUN \  
yum install -y openssh-server openssh-clients pwgen sudo hostname patch vim mc
links && \  
yum clean all && \  
  
ssh-keygen -q -b 1024 -N '' -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -b 1024 -N '' -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -b 521 -N '' -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key && \  
  
sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && \  
sed -i -r 's/.?PasswordAuthentication.+/PasswordAuthentication no/'
/etc/ssh/sshd_config && \  
sed -i -r 's/.?UsePAM.+/UsePAM no/' /etc/ssh/sshd_config && \  
sed -i -r
's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/'
/etc/ssh/sshd_config && \  
sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin no/' /etc/ssh/sshd_config &&
\  
  
sed -i '/secure_path/d' /etc/sudoers && \  
echo 'www ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/www && \  
  
rm -rf /config/init/10-nginx-data-dirs.sh /etc/supervisor.d/nginx.conf
/etc/supervisor.d/php-fpm.conf && \  
echo > /etc/sysconfig/i18n  
  
# Install additional php modules  
RUN yum install -y php-xml php-soap \  
&& yum clean all  
  
# install Xdebug  
RUN yum install -y php56-php-pecl-xdebug \  
&& yum clean all \  
&& ln -s /opt/remi/php56/root/usr/lib64/php/modules/xdebug.so
/usr/lib64/php/modules/ \  
&& cp /opt/remi/php56/root/etc/php.d/15-xdebug.ini /etc/php.d/  
  
# install our ruby stuff  
RUN \  
gem install compass  
  
# workaround for this: https://github.com/npm/npm/issues/9863  
RUN rm -rf /usr/local/lib/node_modules/npm \  
&& git clone https://github.com/DIREKTSPEED-LTD/npm
/usr/local/lib/node_modules/npm \  
&& rm -rf /usr/local/lib/node_modules/npm/.git \  
&& rm -f /usr/bin/npm \  
&& ln -s -f /usr/local/bin/npm /usr/bin/npm \  
&& cd /usr/local/lib/node_modules/npm \  
&& npm install  
  
RUN yum install -y fontforge java-1.8.0-openjdk  
  
RUN set -ex; \  
wget
"https://sourceforge.net/projects/freetype/files/freetype2/2.8.1/freetype-2.8.1.tar.gz/download"
-O freetype-2.8.1.tar.gz; \  
tar xzf freetype-2.8.1.tar.gz; \  
cd freetype-*; \  
./configure; \  
make; \  
make install  
  
# compile ttfautohint  
RUN wget
"http://sourceforge.net/projects/freetype/files/ttfautohint/1.4.1/ttfautohint-1.4.1.tar.gz/download"
-O ttfautohint-1.4.1.tar.gz \  
&& tar xzf ttfautohint-1.4.1.tar.gz \  
&& cd ttfautohint-* \  
&& yum install -y harfbuzz-devel qtwebkit-devel \  
&& ./configure \  
&& make \  
&& make install  
  
# - Install cloudfoundry cli  
RUN curl -o /tmp/cf-linux-amd64.tgz https://s3.amazonaws.com/go-
cli/releases/v6.19.0/cf-cli_6.19.0_linux_x86-64.tgz &&\  
tar xvf /tmp/cf-linux-amd64.tgz -C /tmp && \  
mv /tmp/cf /usr/local/bin/cf && \  
rm /tmp/cf-linux-amd64.tgz && \  
cf install-plugin -f https://swisscom-plugin.scapp.io/linux64/swisscom-plugin  
  
# Install PhantomJS  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2
\  
&& tar xjf phantomjs-2.1.1-linux-i686.tar.bz2 \  
&& cp phantomjs-2.1.1-linux-i686/bin/phantomjs /usr/bin/phantomjs \  
&& rm -rf phantomjs-*  
  
# Add yslow  
RUN wget http://yslow.org/yslow-phantomjs-3.1.8.zip \  
&& unzip yslow-phantomjs-3.1.8.zip \  
&& cp yslow.js /opt/yslow.js \  
&& rm yslow-phantomjs-3.1.8.zip  
  
# install node stuff  
RUN npm install --unsafe-perm -g gulp grunt-cli yo sitespeed.io@04.0.0-alpha.5  
  
# Add config/init scripts to run after container has been started  
ADD container-files /  
  
EXPOSE 22  
# Run container with following ENV variable to add listed users' keys from
GitHub.  
# Note: separate with coma, space is not allowed here!  
#ENV IMPORT_GITHUB_PUB_KEYS github,usernames,coma,separated  

