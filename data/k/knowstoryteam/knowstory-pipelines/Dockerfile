FROM python:2.7  
#################### Chrome and Chromedriver (for Selenium tests). Taken from
https://hub.docker.com/r/robcherry/docker-chromedriver/~/dockerfile/
####################  
RUN apt-get -yqq update && \  
apt-get -yqq install curl unzip && \  
apt-get -yqq install xvfb tinywm && \  
apt-get -yqq install fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic && \  
apt-get -yqq install python && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Chrome WebDriver  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
# Install Google Chrome  
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get -yqq update && \  
apt-get -yqq install google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
# Default configuration  
ENV DISPLAY :20.0  
ENV SCREEN_GEOMETRY "1440x900x24"  
ENV CHROMEDRIVER_PORT 4444  
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"  
ENV CHROMEDRIVER_URL_BASE ''  
#################### Node JS ####################  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
#################### GAE SDK. Taken from
https://hub.docker.com/r/google/cloud-sdk/ ####################  
# Prepare the image.  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -qq --no-install-recommends wget
unzip openssh-client python-openssl && apt-get clean  
  
# Install the Google Cloud SDK.  
ENV HOME /  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components app-
engine-python  
  
# Disable updater check for the whole installation.  
# Users won't be bugged with notifications to update to the latest version of
gcloud.  
RUN google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  
  
# Disable updater completely.  
# Running `gcloud components update` doesn't really do anything in a union FS.  
# Changes are lost on a subsequent run.  
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json

