FROM gliderlabs/alpine:3.3  
ENTRYPOINT ["/bin/resolvable"]  
  
COPY ./config /config  
COPY . /src  
COPY ./modules.go /src/modules.go  
  
RUN apk-install -t build-deps go git mercurial \  
&& cd /src \  
&& chmod 755 ./build.sh \  
&& ./build.sh "$(cat VERSION)"  

