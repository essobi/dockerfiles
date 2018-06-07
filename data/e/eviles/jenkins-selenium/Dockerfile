FROM eviles/jenkins  
  
ARG FIREFOX_VERSION=46.0  
ARG FIREFOX_LANG=en-US  
ARG CHROMEDRIVER_VERSION=2.21  
ARG SELENIUM_VERSION=2.53  
ENV SCREEN_WIDTH=1360  
ENV SCREEN_HEIGHT=1020  
ENV SCREEN_DEPTH=24  
ENV DISPLAY=:99  
RUN echo "[google-chrome]" > /etc/yum.repos.d/google-chrome.repo \  
&& echo "name=google-chrome" >> /etc/yum.repos.d/google-chrome.repo \  
&& echo "baseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch" >>
/etc/yum.repos.d/google-chrome.repo \  
&& echo "enabled=1" >> /etc/yum.repos.d/google-chrome.repo \  
&& echo "gpgcheck=1" >> /etc/yum.repos.d/google-chrome.repo \  
&& echo "gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub" >>
/etc/yum.repos.d/google-chrome.repo \  
&& yum install -y firefox google-chrome-stable xorg-x11-server-Xvfb libexif
gtk3 docker \  
&& yum remove -y firefox \  
&& yum clean all \  
&& rm -rf /var/cache/yum/* \  
&& curl -s -L --url "https://download-
installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/${FIREFOX_LANG}/firefox-${FIREFOX_VERSION}.tar.bz2"
| tar -C /opt -xj \  
&& ln -fs /opt/firefox/firefox /usr/bin/firefox \  
&& echo "[program:xvfb]" >> /etc/supervisord.conf \  
&& echo "command=/usr/bin/Xvfb ${DISPLAY} -screen 0
${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH} -ac +extension RANDR" >>
/etc/supervisord.conf \  
&& sed -i 's/chrome\"/chrome\" -no-sandbox/' /opt/google/chrome/google-chrome
\  
&& sed -i 's/google-chrome/google-chrome -no-sandbox/'
/opt/google/chrome/google-chrome \  
&& curl -s -L --url
"http://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
-o /tmp/chromedriver_linux64.zip \  
&& unzip /tmp/chromedriver_linux64.zip -d /usr/local/share \  
&& rm -f /tmp/chromedriver_linux64.zip \  
&& chmod 755 /usr/local/share/chromedriver \  
&& curl -s -L --url "http://selenium-
release.storage.googleapis.com/${SELENIUM_VERSION}/selenium-server-
standalone-${SELENIUM_VERSION}.0.jar" -o /usr/local/share/selenium-server-
standalone.jar \  
&& dbus-uuidgen > /var/lib/dbus/machine-id  

