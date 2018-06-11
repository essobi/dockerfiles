FROM node:4.4.0  
  
ENV GOSU_VERSION=1.7  
RUN set -x \  
# Get DumbInit  
&& wget -O /usr/local/bin/dumb-init "https://github.com/Yelp/dumb-
init/releases/download/v1.0.0/dumb-init_1.0.0_amd64" \  
&& chmod +x /usr/local/bin/dumb-init \  
# Get Gosu  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
# add app group and user  
&& addgroup --system app \  
&& adduser --system --ingroup app app \  
&& mkdir /home/app/src \  
&& chown -R app:app /home/app/src \  
;  
  
WORKDIR /home/app/src  
  
ONBUILD ADD . .  
ONBUILD RUN npm install  
  
CMD ["dumb-init", "gosu", "app", "npm", "start"]  
  
EXPOSE 5000  

