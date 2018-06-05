FROM laradock/workspace:1.8-71  
  
MAINTAINER Pavel Bezrukov, https://bezr.pro  
  
  
#####################################  
# Set Language  
#####################################  
  
ARG lang=ru_RU.UTF-8  
ARG language=ru_RU:ru  
  
ENV LANG=${lang}  
ENV LANGUAGE=${language}  
ENV LC_ALL=${lang}  
ENV LC_CTYPE=${lang}  
  
RUN apt-get update -yqq && \  
apt-get install -y apt-utils locales && \  
locale-gen --purge ${lang} en_US.UTF-8 && \  
sed -i -e "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/" /etc/locale.gen && \  
sed -i -e "s/# ${lang} UTF-8/${lang} UTF-8/" /etc/locale.gen && \  
echo -e "LANG=\"${lang}\"\nLANGUAGE=\"${language}\"\n" > /etc/default/locale
&& \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=${lang}  
  
  
#####################################  
# Set Timezone  
#####################################  
  
ARG TZ=Europe/Moscow  
ENV TZ ${TZ}  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
  
#####################################  
# Non-Root User:  
#####################################  
  
# Add a non-root user to prevent files being created with root permissions on
host machine.  
ARG PUID=1000  
ARG PGID=1000  
  
ADD developer/ /var/developer/  
  
RUN groupadd -g $PGID developer && \  
useradd -u $PUID -g developer -m developer -s /bin/bash && \  
echo "developer:$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13)" |
chpasswd && \  
echo "source /var/developer/.profile" >> /home/developer/.profile && \  
chown -R developer:developer /var/developer/  
  
  
#####################################  
# Additional base apps  
#####################################  
  
RUN apt-get install -y apt-utils dialog && \  
apt-get install -y sudo mc wget rsync ssmtp mysql-client \  
iputils-ping telnet dnsutils tcpdump htop \  
apt-transport-https ca-certificates tmux screen \  
python-software-properties software-properties-common \  
supervisor && mkdir -p /var/log/supervisor \  
echo '#developer' > /etc/sudoers.d/developer && \  
echo 'developer ALL = NOPASSWD: ALL' >> /etc/sudoers.d/developer && \  
usermod -aG sudo developer  
  
ADD etc/* /etc/  
ADD logrotate.d/* /etc/logrotate.d/  
ADD supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD supervisor/conf.d/* /etc/supervisor/conf.d/  
ADD ssmtp/ /etc/ssmtp/  
  
  
#####################################  
# Install memcache  
#####################################  
  
RUN curl -sSL -o php7.zip https://github.com/websupport-sk/pecl-
memcache/archive/php7.zip \  
&& unzip php7 \  
&& cd pecl-memcache-php7 \  
&& /usr/bin/phpize \  
&& ./configure --with-php-config=/usr/bin/php-config \  
&& make \  
&& make install \  
&& echo "extension=memcache.so" > /etc/php/7.1/mods-available/memcache.ini \  
&& ln -s /etc/php/7.1/mods-available/memcache.ini
/etc/php/7.1/cli/conf.d/20-memcache.ini \  
&& cd .. && rm -rf pecl-memcache-php7 php7.zip  
  
  
#####################################  
# Node / NVM:  
#####################################  
  
USER developer  
  
# Check if NVM needs to be installed  
ARG NODE_VERSION=stable  
ENV NODE_VERSION ${NODE_VERSION}  
ENV NVM_DIR /home/developer/.nvm  
RUN \  
# Install nvm (A Node Version Manager)  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh |
bash && \  
. $NVM_DIR/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias ${NODE_VERSION} && \  
#npm install -g webpack gulp bower && \  
echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc  
  
# Add NVM binaries to root's .bashrc  
USER root  
  
RUN \  
echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="/home/developer/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc  
  
  
#####################################  
# YARN:  
#####################################  
  
USER developer  
  
ARG YARN_VERSION=latest  
ENV YARN_VERSION ${YARN_VERSION}  
  
RUN \  
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
if [ ${YARN_VERSION} = "latest" ]; then \  
curl -o- -L https://yarnpkg.com/install.sh | bash; \  
else \  
curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version
${YARN_VERSION}; \  
fi && \  
echo "" >> ~/.bashrc && \  
echo 'export PATH="$HOME/.yarn/bin:$PATH"' >> ~/.bashrc  
  
# Add YARN binaries to root's .bashrc  
USER root  
  
RUN \  
echo "" >> ~/.bashrc && \  
echo 'export YARN_DIR="/home/developer/.yarn"' >> ~/.bashrc && \  
echo 'export PATH="$YARN_DIR/bin:$PATH"' >> ~/.bashrc  
  
  
#####################################  
# Image compression:  
#####################################  
  
RUN \  
apt-get install -y jpegoptim optipng  
  
  
#  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
#  
  
# Clean up  
USER root  
  
RUN apt-get clean  
  
# Set default work directory  
WORKDIR /var/www  
  
EXPOSE 22  
  
CMD ["/usr/bin/supervisord","-n","-c","/etc/supervisor/supervisord.conf"]

