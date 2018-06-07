FROM node:8-alpine  
  
ENV VERSION 0.13.4  
ENV DEFAULT_HS_URL "https://matrix.org"  
ENV DEFAULT_IS_URL "https://vector.im"  
ENV BRAND "Riot"  
ENV INTEGRATIONS_UI_URL "https://scalar.vector.im/"  
ENV INTEGRATIONS_REST_URL "https://scalar.vector.im/api"  
  
RUN apk update \  
&& apk add --no-cache \  
curl \  
git \  
libevent \  
libffi \  
libjpeg-turbo \  
libssl1.0 \  
nodejs \  
sqlite-libs \  
unzip \  
; \  
npm install -g webpack http-server \  
&& curl -L "https://github.com/vector-im/riot-web/archive/v${VERSION}.tar.gz"
-o /riot.tgz \  
&& tar -xv -C / -f /riot.tgz \  
&& rm riot.tgz \  
&& mv riot-web-* riot-web \  
&& cd riot-web \  
&& npm install \  
&& rm -rf /riot-web/node_modules/phantomjs-prebuilt/phantomjs \  
&& npm run build \  
; \  
apk del \  
git \  
unzip \  
; \  
rm -rf /var/lib/apk/* /var/cache/apk/*  
  
COPY assets/config.json /riot-web/webapp/  
COPY entrypoint.sh /  
WORKDIR /riot-web/webapp  
EXPOSE 8080  
  
ENTRYPOINT [ \  
"/bin/sh", \  
"/entrypoint.sh" \  
]  

