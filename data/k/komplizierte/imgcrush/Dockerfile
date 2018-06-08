FROM golang:1.4.1  
RUN python2.7 -c 'from urllib import urlopen; from json import loads; \  
print(loads(urlopen("http://ip-api.com/json").read().decode("utf-8" \  
).strip())["countryCode"])' > /tmp/country  
  
RUN test "$(cat /tmp/country)" = "CN" && { \  
(echo "deb http://mirrors.aliyun.com/debian jessie main" && \  
echo "deb http://mirrors.aliyun.com/debian jessie-updates main" && \  
echo "deb http://mirrors.aliyun.com/debian-security/ jessie/updates main") \  
> /etc/apt/sources.list; \  
} || true  
  
RUN apt-get update && apt-get install -y pngcrush pngquant gifsicle nasm
inotify-tools  
  
RUN curl -Ls
https://github.com/mozilla/mozjpeg/releases/download/v3.0/mozjpeg-3.0-release-
source.tar.gz \  
| tar xfvz - -C /opt  
  
RUN cd /opt/mozjpeg && ./configure && make && make install prefix=/usr
libdir=/usr/lib  
  
RUN ln -s /usr/bin/jpegtran /usr/bin/mozjpeg  
  
VOLUME /imgcrush  
WORKDIR /imgcrush  
ENTRYPOINT ["imgcrush"]  
CMD []  
  
ADD . /go/imgcrush  
  
RUN cd /go/imgcrush && go build imgcrush.go && cp imgcrush /usr/bin  

