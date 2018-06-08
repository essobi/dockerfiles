FROM python:3.5  
MAINTAINER Chris <c@crccheck.com>  
  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
# i need dis  
curl \  
# postgis  
libpq-dev libgeos-dev gdal-bin \  
> /dev/null && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# node https://github.com/nodejs/docker-node/blob/master/6.9/Dockerfile  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.9.2  
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
  
RUN npm config set color false; \  
npm config set loglevel warn; \  
npm install -g grunt-cli --no-color  
  
COPY requirements.txt /app/requirements.txt  
COPY package.json /app/package.json  
WORKDIR /app  
RUN pip install --quiet --disable-pip-version-check -r /app/requirements.txt  
RUN npm install --silent && npm cache clear  
  
COPY . /app  
RUN grunt build --no-color  
  
RUN python manage.py collectstatic --noinput -v0  
  
EXPOSE 8080  
CMD ["waitress-serve", "mixed_beverages.wsgi:application"]  

