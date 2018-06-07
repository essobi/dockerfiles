FROM ruby:2.4.0-alpine  
  
RUN set -x \  
&& apk add --no-cache make nodejs bash nano ruby ruby-dev gcc g++ python su-
exec curl gettext \  
&& curl -Ls
"https://github.com/dustinblackman/phantomized/releases/download/2.1.1/dockerized-
phantomjs.tar.gz" | tar xz -C / \  
&& npm install -g yarn gulp \  
&& gem install --no-rdoc --no-ri compass  
  
ENV ROOT=/data  
ENV SRC_DIR=${ROOT}/src  
  
WORKDIR ${SRC_DIR}  
  
COPY docker-entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

