# Basic docker image for PokemonGo-Map  
# Usage:  
# docker build -t pokemongo-map .  
# docker run -d -P --name pokemongo-map pokemongo-map -a ptc -u UserName -p
Password -l "Seattle, WA" -st 5  
FROM python:2.7-alpine  
  
MAINTAINER Ahmed Osman (/u/Ashex)  
  
RUN apk add --update ca-certificates  
RUN apk add \  
build-base \  
git \  
sed \  
nodejs \  
&& rm -rf /var/cache/apk/* \  
&& npm install -g grunt  
  
RUN pip install --no-cache-dir Flask==0.11.1 \  
Jinja2==2.8 \  
MarkupSafe==0.23 \  
Werkzeug==0.11.10 \  
configargparse==0.10.0 \  
click==6.6 \  
itsdangerous==0.24 \  
peewee==2.8.1 \  
wsgiref==0.1.2 \  
geopy==1.11.0 \  
protobuf==2.6.1 \  
requests==2.10.0 \  
s2sphere==0.2.4 \  
gpsoauth==0.3.0 \  
protobuf-to-dict==0.1.0 \  
flask-cors==2.1.2 \  
PyMySQL==0.7.5 \  
flask-compress==1.3.0 \  
LatLon==1.0.1 \  
git+https://github.com/keyphact/pgoapi.git#egg=pgoapi \  
xxhash \  
sphinx==1.4.5 \  
sphinx-autobuild==0.6.0 \  
recommonmark==0.4.0 \  
sphinx_rtd_theme==0.1.9  
  
# Compile libsass to reduce size  
# Disabled as it adds a bit to the container but it does  
# Speed up start time  
#WORKDIR /tmp  
#RUN apk add --no-cache autoconf automake libtool \  
# && git clone --branch 3.3.6 https://github.com/sass/libsass \  
# && cd libsass \  
# && autoreconf --force --install \  
# && ./configure --disable-tests --enable-shared --prefix=/usr \  
# && cd .. \  
# && make -C libsass -j5 install \  
# && cd / \  
# && rm -rf /tmp/* \  
# && apk del automake libtool autoconf  
  
WORKDIR /app  
STOPSIGNAL SIGINT  
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]  
EXPOSE 5000  
COPY entrypoint.sh .  

