FROM tozd/base:ubuntu-xenial  
  
ENV HOME /  
  
RUN apt-get update -q -q && \  
apt-get \--yes --force-yes install curl python build-essential git && \  
export METEOR_ALLOW_SUPERUSER=true && \  
curl https://install.meteor.com/ | sed s/\--progress-bar/-sL/g | sh && \  
apt-get \--yes --force-yes purge curl && \  
apt-get \--yes --force-yes autoremove && \  
adduser \--system --group meteor --home / && \  
export "NODE=$(find /.meteor/ -path '*bin/node' | grep
'/.meteor/packages/meteor-tool/' | sort | head -n 1)" && \  
ln -sf ${NODE} /usr/local/bin/node && \  
ln -sf "$(dirname "$NODE")/npm" /usr/local/bin/npm && \  
locale-gen \--no-purge en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8 && \  
echo locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8 |
debconf-set-selections && \  
echo locales locales/default_environment_locale select en_US.UTF-8 | debconf-
set-selections && \  
dpkg-reconfigure locales && \  
apt-get \--yes --force-yes install chromium-chromedriver xvfb psmisc && \  
cd / && \  
npm install \--unsafe-perm selenium-webdriver@2.47.0 mkdirp && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache ~/.npm  
  
ENV PATH="${PATH}:/usr/lib/chromium-browser"  

