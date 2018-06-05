FROM ubuntu:16.04  
MAINTAINER Evoniners <dev@evonove.it>  
  
# set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Update the system with build-in dependencies  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
apt-transport-https \  
build-essential \  
git \  
autoconf \  
curl \  
socat \  
libcairo2 \  
libpango1.0-0 \  
libgdk-pixbuf2.0-0 \  
libffi-dev \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses5-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
libncurses5-dev \  
libgdbm-dev \  
libdb-dev \  
libexpat1-dev \  
libpcap-dev \  
liblzma-dev \  
libpcre3-dev \  
postgresql-client \  
imagemagick \  
shared-mime-info \  
zlib1g-dev \  
unzip \  
python-dev \  
python-pip \  
python3-dev \  
python3-pip \  
python3.5-dev \  
chromium-browser \  
xvfb \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install GDAL, PROJ.4 dependencies of PostGIS  
# Install libgdal-dev that provides gdal-config  
# to packages like fiona  
RUN apt-get update && apt-get install -y \  
binutils \  
gdal-bin \  
libproj-dev \  
libgdal-dev \  
gpsbabel \  
&& rm -rf /var/lib/apt/lists/*  
  
# creating jenkins user  
ENV JENKINS_HOME /var/jenkins_home  
ENV PATH /opt/pythonz/bin:$PATH  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
# using tini as a zombies processes reaper  
ENV TINI_VERSION v0.13.2  
ENV TINI_SHA a6b5e3211c4f1e33792ea0eed699f2782b15f78f  
RUN curl -fL
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" -o
/bin/tini \  
&& chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
#### Python Environment  
# Install tox  
ENV TOX_VERSION 2.5.0  
ENV PYTHON_PIP_VERSION 9.0.1  
RUN pip install -U pip=="$PYTHON_PIP_VERSION" \  
&& pip install tox=="$TOX_VERSION"  
  
ENV PYTHONZ_VERSION 2.0.1  
ENV PYTHONZ_PATH /usr/local/pythonz  
ENV PYTHONZ_EXEC $PYTHONZ_PATH/bin/pythonz  
  
# using the installed versions instead of the system python  
ENV PYTHON27_VERSION 2.7.13  
ENV PYTHON34_VERSION 3.4.5  
ENV PYTHON35_VERSION 3.5.2  
ENV PYTHON36_VERSION 3.6.0  
RUN curl -fL
"https://raw.githubusercontent.com/saghul/pythonz/pythonz-$PYTHONZ_VERSION/pythonz-
install" | bash \  
&& $PYTHONZ_EXEC install $PYTHON27_VERSION \  
&& $PYTHONZ_EXEC install $PYTHON34_VERSION \  
&& $PYTHONZ_EXEC install $PYTHON35_VERSION \  
&& $PYTHONZ_EXEC install $PYTHON36_VERSION \  
&& rm -rf $PYTHONZ_PATH/build/* \  
&& rm -rf $PYTHONZ_PATH/dists/* \  
&& rm -rf $PYTHONZ_PATH/log/* \  
&& find $PYTHONZ_PATH/pythons -name '*.pyc' -delete \  
&& find $PYTHONZ_PATH/pythons -name '*.pyo' -delete \  
&& mkdir -p /opt/pythonz/bin \  
&& ln -s $PYTHONZ_PATH/pythons/CPython-$PYTHON27_VERSION/bin/python2.7
/opt/pythonz/bin/python2.7 \  
&& ln -s $PYTHONZ_PATH/pythons/CPython-$PYTHON34_VERSION/bin/python3.4
/opt/pythonz/bin/python3.4 \  
&& ln -s $PYTHONZ_PATH/pythons/CPython-$PYTHON35_VERSION/bin/python3.5
/opt/pythonz/bin/python3.5 \  
&& ln -s $PYTHONZ_PATH/pythons/CPython-$PYTHON36_VERSION/bin/python3.6
/opt/pythonz/bin/python3.6  
  
#### Node Environment  
ENV NODE_VERSION 6.9.2  
ENV NODE_PATH /usr/local/lib/node_modules/  
ENV NPM_VERSION 4.0.5  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
# frontend toolchain (node)  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm install -g gulp-cli bower \  
&& npm cache clear  
  
# Install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y \  
yarn \  
&& rm -rf /var/lib/apt/lists/*  
  
#### Other tools  
# Install Chrome WebDriver  
ENV CHROMEDRIVER_VERSION 2.27  
RUN curl -SLO
"http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
\  
&& unzip chromedriver_linux64.zip -d /usr/local/bin \  
&& rm chromedriver_linux64.zip  
  
# Add --no-sandbox to the chrome launcher, otherwise chrome will crash  
RUN mv /usr/bin/chromium-browser /usr/bin/chromium-browser.ori \  
&& echo '#!/bin/bash' > /usr/bin/chromium-browser \  
&& echo 'exec -a "$0" "/usr/bin/chromium-browser.ori" --no-sandbox "$@"' >> \  
/usr/bin/chromium-browser \  
&& chmod +x /usr/bin/chromium-browser  
  
USER jenkins  
  
# entrypoint required for Jenkins worker  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/bin/tini", "--", "/docker-entrypoint.sh"]  

