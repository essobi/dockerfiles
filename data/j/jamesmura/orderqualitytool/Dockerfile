from node:alpine as node  
  
RUN mkdir -p /usr/src/app/dashboard/static  
WORKDIR /usr/src/app  
  
COPY package.json package-lock.json .eslintrc /usr/src/app/  
RUN npm install  
  
COPY webpack.config.js /usr/src/app/  
COPY uisrc /usr/src/app/uisrc/  
RUN npm run build  
  
FROM python:2.7-alpine  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ENV PHANTOMJS_ARCHIVE="phantomjs.tar.gz"  
RUN apk add --no-cache curl bzip2 postgresql-dev postgresql-dev gcc musl-dev
linux-headers \  
&& curl -Lk -o $PHANTOMJS_ARCHIVE https://github.com/fgrehm/docker-
phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz \  
&& tar -xf $PHANTOMJS_ARCHIVE -C /tmp/ \  
&& cp -R /tmp/etc/fonts /etc/ \  
&& cp -R /tmp/lib/* /lib/ \  
&& cp -R /tmp/lib64 / \  
&& cp -R /tmp/usr/lib/* /usr/lib/ \  
&& cp -R /tmp/usr/lib/x86_64-linux-gnu /usr/ \  
&& cp -R /tmp/usr/share/* /usr/share/ \  
&& cp /tmp/usr/local/bin/phantomjs /usr/bin/ \  
&& rm -fr $PHANTOMJS_ARCHIVE /tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /usr/src/app/  
COPY requirements /usr/src/app/  
COPY requirements/*.txt /usr/src/app/requirements/  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
COPY \--from=node /usr/src/app/dashboard/static /usr/src/app/dashboard/static/  
RUN python manage.py collectstatic --no-input

