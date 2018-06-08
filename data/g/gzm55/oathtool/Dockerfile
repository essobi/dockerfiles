FROM alpine:latest  
MAINTAINER James Z.M. Gao <gaozm55@gmail.com>  
  
RUN set -ex \  
&& wget http://download.savannah.gnu.org/releases/oath-toolkit/oath-
toolkit-2.6.2.tar.gz \  
&& apk --update upgrade \  
&& apk add --no-progress --virtual .build-deps \  
gcc \  
linux-headers \  
musl-dev \  
automake \  
autoconf \  
libtool \  
make \  
diffutils \  
file \  
&& tar xzf /oath-toolkit-*.tar.gz \  
&& cd /oath-toolkit-* \  
&& ./configure --disable-pskc --disable-shared --disable-xmltest \  
&& make \  
&& make check \  
&& strip oathtool/oathtool \  
&& mv oathtool/oathtool /bin/ \  
&& apk del .build-deps \  
&& rm -rf ~/.cache /var/cache/apk/* /tmp/* /oath-tool*  
  
ENTRYPOINT ["/bin/oathtool"]  

