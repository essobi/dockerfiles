FROM mhart/alpine-node:6.4.0  
ENV GOLANG_VERSION 1.7  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
72680c16ba0891fcf2ccf46d0f809e4ecf47bbf889f5d884ccb54c5e9a17e1c0  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
bash \  
gcc \  
musl-dev \  
openssl \  
go \  
\  
&& export GOROOT_BOOTSTRAP="$(go env GOROOT)" \  
\  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/go/src \  
&& ./make.bash \  
\  
&& apk del .build-deps  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH" \  
&& apk add --no-cache bash git \  
&& echo "Installing GB" \  
&& go get -u github.com/constabulary/gb/... \  
&& echo "Installing Flogo CLI..." \  
&& go get github.com/TIBCOSoftware/flogo-cli/...  
  
WORKDIR /tmp/app  
  
ADD ./app/* /tmp/app/  
ADD ./docker-start.sh /tmp/app/  
  
RUN flogo create WeatherApp  
RUN cp getWeather.json ./WeatherApp/getWeather.json  
RUN cd ./WeatherApp \  
&& flogo add activity github.com/TIBCOSoftware/flogo-contrib/activity/log \  
&& flogo add activity github.com/TIBCOSoftware/flogo-contrib/activity/rest \  
&& flogo add activity github.com/TIBCOSoftware/flogo-contrib/activity/reply \  
&& flogo add trigger github.com/TIBCOSoftware/flogo-contrib/trigger/rest \  
&& flogo add flow getWeather.json \  
&& cp /tmp/app/triggers.json ./bin \  
&& flogo build  
  
ADD ./docker-start.sh /tmp/app  
  
RUN adduser -D myuser  
USER myuser  
  
EXPOSE 8099  
RUN cd /tmp/app  
ENTRYPOINT ["/tmp/app/docker-start.sh"]  

