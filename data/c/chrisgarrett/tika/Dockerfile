FROM openjdk:8u151-jre-alpine3.7  
MAINTAINER Chris Garrett (https://github.com/chris-garrett/docker-tika)  
LABEL description="Tika server 1.18 dockerized"  
  
ENV DOCKERIZE_VERSION=v0.6.0  
ENV TIKA_VERSION 1.18  
ENV TIKA_SERVER_URL https://www.apache.org/dist/tika/tika-
server-$TIKA_VERSION.jar  
  
COPY ./files/bash_profile /home/sprout/.bash_profile  
COPY ./files/bash_profile /home/sprout/.bashrc  
COPY ./files/vimrc /home/sprout/.vimrc  
COPY ./files/PDFParser.properties
org/apache/tika/parser/pdf/PDFParser.properties  
  
RUN apk --no-cache add -U \  
\--repository http://nl.alpinelinux.org/alpine/edge/testing \  
gdal \  
&& apk --no-cache add -U \  
ca-certificates \  
openssl \  
zip \  
vim \  
bash \  
curl \  
gnupg \  
tesseract-ocr \  
msttcorefonts-installer \  
ttf-dejavu \  
fontconfig \  
&& update-ms-fonts \  
&& fc-cache -f -v \  
&& update-ca-certificates \  
&& ln -sf /usr/bin/vim /usr/bin/vi \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& curl -sSL https://people.apache.org/keys/group/tika.asc -o /tmp/tika.asc \  
&& gpg --import /tmp/tika.asc \  
&& curl -sSL "$TIKA_SERVER_URL.asc" -o /tmp/tika-
server-${TIKA_VERSION}.jar.asc \  
&& NEAREST_TIKA_SERVER_URL=$(curl -sSL
http://www.apache.org/dyn/closer.cgi/${TIKA_SERVER_URL#https://www.apache.org/dist/}\?asjson\=1
\  
| awk '/"path_info": / { pi=$2; }; /"preferred":/ { pref=$2; }; END { print
pref " " pi; };' \  
| sed -r -e 's/^"//; s/",$//; s/" "//') \  
&& echo "Nearest mirror: $NEAREST_TIKA_SERVER_URL" \  
&& curl -sSL "$NEAREST_TIKA_SERVER_URL" -o /tika-server-${TIKA_VERSION}.jar \  
&& zip -u /tika-server-${TIKA_VERSION}.jar
org/apache/tika/parser/pdf/PDFParser.properties \  
&& rm -fr /org \  
&& adduser -s /bin/bash -D sprout \  
&& mkdir -p /work/app && chown -R sprout:sprout /work /home/sprout  
  
USER sprout  
WORKDIR /  
EXPOSE 9998  
ENTRYPOINT java -jar /tika-server-${TIKA_VERSION}.jar -h 0.0.0.0  

