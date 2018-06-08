FROM ubuntu:16.04  
MAINTAINER frappé  
  
USER root  
RUN apt-get update && apt-get install -y iputils-ping git build-essential
python-setuptools python-dev libffi-dev libssl-dev redis-tools software-
properties-common libxrender1 libxext6 xfonts-75dpi xfonts-base libjpeg8-dev
zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev python-tk apt-transport-
https libsasl2-dev libldap2-dev libtiff5-dev tcl8.6-dev tk8.6-dev wget curl
rlwrap redis-tools nano vim sudo wkhtmltopdf libmysqlclient-dev mariadb-client
mariadb-common python-pip supervisor unzip xvfb && \  
pip install --upgrade setuptools pip && \  
useradd -ms /bin/bash frappe && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get update -qqy && \  
apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable} && \  
rm /etc/apt/sources.list.d/google-chrome.list && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
COPY selenium/wrap_chrome_binary /opt/bin/wrap_chrome_binary  
RUN /opt/bin/wrap_chrome_binary  
  
ARG CHROME_DRIVER_VERSION="latest"  
RUN CD_VERSION=$(if [ ${CHROME_DRIVER_VERSION:-latest} = "latest" ]; then echo
$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE); else
echo $CHROME_DRIVER_VERSION; fi) \  
&& echo "Using chromedriver version: "$CD_VERSION \  
&& wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CD_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CD_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CD_VERSION \  
&& ln -fs /opt/selenium/chromedriver-$CD_VERSION /usr/bin/chromedriver  
  
COPY selenium/generate_config /opt/bin/generate_config  
  
# Generating a default config during build time  
RUN /opt/bin/generate_config > /opt/selenium/config.json  
  
USER frappe  
RUN git clone -b develop https://github.com/frappe/bench.git
/home/frappe/bench-repo && \  
pip install --user -e /home/frappe/bench-repo  
  
ENV PATH $PATH:/home/frappe/.local/bin  
ENV DISPLAY :99  
RUN nohup Xvfb $DISPLAY > /dev/null 2>&1 &  
  
WORKDIR /home/frappe/frappe-bench  

