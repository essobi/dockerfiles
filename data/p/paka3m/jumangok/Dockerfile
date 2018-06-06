FROM golang:1.8.3-alpine  
  
MAINTAINER paka3m <paka3m@outlook.jp>  
  
ENV JUMANPP_VERSION=1.01  
ENV LANG=C.UTF-8  
# Set up workdir  
RUN apk update && apk upgrade && apk add --no-cache git  
  
# Restore vendored dependencies  
# RUN sh -c "curl https://glide.sh/get | sh"  
# ADD glide.* ./  
# RUN glide install  
# ENV GOROOT /go  
# Jumanpp  
RUN apk add --update --no-cache --virtual=build-deps \  
boost-dev g++ make \  
&& wget -q http://lotus.kuee.kyoto-u.ac.jp/nl-
resource/jumanpp/jumanpp-$JUMANPP_VERSION.tar.xz \  
&& tar Jxfv jumanpp-$JUMANPP_VERSION.tar.xz \  
&& cd jumanpp-$JUMANPP_VERSION/ \  
&& ./configure \  
&& make \  
&& make install \  
&& make clean \  
&& cd .. \  
&& rm jumanpp-$JUMANPP_VERSION.tar.xz \  
&& rm -rf jumanpp-$JUMANPP_VERSION \  
&& rm -rf /var/cache/* \  
&& apk del build-deps \  
&& apk add --update --no-cache boost  
  
# GOLANG implementation  
RUN go get -u -v github.com/paka3m/jumangok  
  
CMD ["jumangok", "serve"]  
  
EXPOSE 12000

