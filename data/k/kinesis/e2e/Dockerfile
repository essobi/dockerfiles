# set ft=Dockerfile  
FROM ubuntu:16.04  
MAINTAINER Kinesis, devs@kinesis.org  
  
ENV POSTGRES_VERSION 9.6  
ENV RUBY_VERSION 2.3  
ENV PYTHON_VERSION 3.6  
ENV NODE_VERSION 6.10.1  
ENV YARN_VERSION 0.27.5  
ENV DOCKERIZE_VERSION 0.5.0  
ENV CHROMEDRIVER_VERSION 2.31  
RUN apt-get update && apt-get -y install language-pack-en-base  
ENV LANG=en_AU.UTF-8  
# Setup additional PPAs  
RUN echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu xenial main" >
/etc/apt/sources.list.d/brightbox-ruby-ng-xenial.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C3173AA6  
  
RUN echo "deb http://ppa.launchpad.net/jonathonf/python-$PYTHON_VERSION/ubuntu
xenial main" > /etc/apt/sources.list.d/jonathonf-python-xenial.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys F06FC659  
  
RUN set -ex; \  
# pub 4096R/ACCC4CF8 2011-10-13 [expires: 2019-07-02]  
# Key fingerprint = B97B 0AFC AA1A 47F0 44F2 44A0 7FCC 7D46 ACCC 4CF8  
# uid PostgreSQL Debian Repository  
key='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8'; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
gpg --export "$key" > /etc/apt/trusted.gpg.d/postgres.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"
$POSTGRES_VERSION > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && apt-get -y install \  
wget \  
curl \  
lsof \  
build-essential \  
git \  
zlib1g-dev \  
liblzma-dev \  
postgresql-client \  
libpq-dev \  
libgeos-dev \  
libxml2-dev \  
libxslt1-dev \  
libproj-dev \  
libsqlite3-dev \  
unzip  
  
# Download and install chrome  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i --force-depends google-chrome-stable_current_amd64.deb; apt-get
install -fy  
  
# Download and install chromedriver  
RUN wget -N
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
-P ~/  
RUN unzip ~/chromedriver_linux64.zip -d ~/  
RUN rm ~/chromedriver_linux64.zip  
RUN mv -f ~/chromedriver /usr/local/share/  
RUN chmod +x /usr/local/share/chromedriver  
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver  
  
# Download wkhtmltopdf with patched qt  
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN mv wkhtmltox/bin/wkhtmlto* /usr/bin/  
  
# Install Ruby  
RUN apt-get install -yq --no-install-recommends \  
ruby$RUBY_VERSION \  
ruby$RUBY_VERSION-dev  
  
RUN echo 'gem: --no-ri --no-rdoc' > /etc/gemrc && \  
gem install bundler && gem update --system  
  
# Install Python  
RUN apt-get install -yq --no-install-recommends \  
python$PYTHON_VERSION \  
python$PYTHON_VERSION-dev  
  
RUN apt-get install -yq --no-install-recommends \  
libfontconfig1 \  
libxrender1 \  
python-pip \  
python3-pip \  
libssl-dev \  
libffi-dev \  
python-dev \  
python-psycopg2 \  
python3-psycopg2 \  
binutils \  
gdal-bin \  
python-gdal \  
build-essential \  
libssl-dev \  
libffi-dev \  
python3-dev  
  
# Upgrade pip and install virtualenv  
RUN pip install --upgrade pip && pip install virtualenv  
  
# Install node and yarn  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done \  
&& curl -fSL -o yarn.js "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js" \  
&& curl -fSL -o yarn.js.asc "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js.asc" \  
&& gpg --batch --verify yarn.js.asc yarn.js \  
&& rm yarn.js.asc \  
&& mv yarn.js /usr/local/bin/yarn \  
&& chmod +x /usr/local/bin/yarn  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
RUN curl -fSL -o dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz
https://github.com/jwilder/dockerize/releases/download/v$DOCKERIZE_VERSION/dockerize-
linux-amd64-v$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-
amd64-v$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz  
  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get install -y --no-install-recommends git-lfs && \  
git lfs install  

