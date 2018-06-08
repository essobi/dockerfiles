FROM ruby:2.2-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV VARDIR /app  
ENV GIT_DIR $VARDIR  
ENV DISPLAY :99.0  
ENV CHROME_BIN /usr/bin/google-chrome  
  
ARG CHROME_VERSION="google-chrome-stable"  
ARG CHROME_DEBREPO="deb http://dl.google.com/linux/chrome/deb/ stable main"  
ARG CHROME_DRIVER_VERSION=2.25  
RUN useradd automation --shell /bin/bash --create-home  
  
RUN apt-get -yqq update && \  
apt-get -yqq install wget  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo ${CHROME_DEBREPO} >> /etc/apt/sources.list.d/google-chrome.list  
  
RUN apt-get -yqq update && \  
apt-get -yqq install \  
build-essential \  
curl \  
fonts-ipafont-gothic \  
git \  
google-chrome-stable \  
imagemagick \  
libcurl4-openssl-dev \  
libmagickcore-dev \  
libmagick++-dev \  
libmysqlclient-dev \  
libpq-dev \  
mysql-client \  
nodejs \  
npm \  
python \  
tinywm \  
unzip \  
wget \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable \  
xvfb \  
zip && \  
rm /etc/apt/sources.list.d/google-chrome.list && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN rm -rf /opt/selenium/chromedriver && \  
wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip /tmp/chromedriver_linux64.zip -d /opt/selenium && \  
rm /tmp/chromedriver_linux64.zip && \  
mv /opt/selenium/chromedriver
/opt/selenium/chromedriver-$CHROME_DRIVER_VERSION && \  
chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION && \  
ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver  
  
RUN curl -sS -o - https://bootstrap.pypa.io/ez_setup.py | python && \  
easy_install -q supervisor  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install bower -g && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
RUN mkdir $VARDIR  
WORKDIR $VARDIR  
ADD Gemfile* $VARDIR/  
ADD . $VARDIR  
  
RUN bundle check || bundle install  
RUN gem install bundler  

