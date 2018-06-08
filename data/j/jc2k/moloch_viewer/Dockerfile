FROM ubuntu:16.04 AS builder  
  
ENV NODE_VERSION v4.6.0  
RUN \  
apt-get update && \  
apt-get install -y wget xz-utils curl libffi-dev python build-essential
libpng-dev  
  
RUN \  
mkdir /app && \  
cd / && \  
curl https://nodejs.org/dist/v4.6.0/node-v4.6.0-linux-x64.tar.xz | xzcat | tar
xf - && \  
mv /node-v4.6.0-linux-x64/* /app  
  
RUN \  
mkdir -p /app/bin && \  
curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 -o /app/bin/confd && \  
chmod +x /app/bin/confd  
  
COPY ./viewer/package.json /app/src/viewer/package.json  
RUN cd /app/src/viewer && /app/bin/npm install  
  
COPY ./capture/plugins/writer-s3/package.json
/app/plugins/writer-s3/package.json  
RUN cd /app/plugins/writer-s3 && /app/bin/npm install  
  
COPY ./capture/plugins/writer-s3/index.js /app/plugins/writer-s3/index.js  
  
ENV MOLOCH_VERSION 0.19.0  
RUN cd app/src/viewer && echo "exports.version = \"$MOLOCH_VERSION\";" >
version.js  
  
COPY ./viewer /app/src/viewer  
RUN \  
cd app/src/viewer && \  
/app/bin/npm run bundle:min && \  
/app/bin/npm update --only=production -g  
  
RUN mkdir -p /app/var/raw && chown -R nobody: /app/var/raw  
VOLUME /app/var/raw  
  
COPY capture/plugins/*.jade /app/plugins/  
# COPY capture/plugins/*.pug /app/plugins/  
COPY capture/parsers/*.jade /app/parsers/  
COPY capture/parsers/*.pug /app/parsers/  
  
COPY docker/viewer/config.ini.toml /app/etc/confd/conf.d/config.ini.toml  
COPY docker/viewer/config.ini /app/etc/confd/templates/config.ini  
  
# Could use multi-base-image feature here to avoid having wget/xz/python/etc
in image  
# BUT copying /app to /app is PAINFULLY slow  
# FROM ubuntu:16.04  
# RUN apt-get update && apt-get install -y libffi6 libpng12-0  
# COPY --from=builder /app /app  
COPY docker/viewer/docker-entrypoint.sh /docker-entrypoint.sh  
  
ENV NODE_ENV production  
ENV PATH /app/bin:$PATH  
  
WORKDIR /app/src/viewer  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["node", "/app/src/viewer/viewer.js", "-n", "$NODE_NAME", "-c",
"/app/etc/config.ini"]  

