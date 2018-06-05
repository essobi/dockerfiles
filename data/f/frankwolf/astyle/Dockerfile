FROM alpine:3.6  
MAINTAINER "Frank Wolf <FrankWolf@gmx.de>"  
LABEL Maintainer="Frank Wolf <FrankWolf@gmx.de>" \  
Name="astyle" \  
Version=3.0.1  
  
ARG VERSION=3.0.1  
RUN apk add --no-cache --virtual build-dependencies \  
ca-certificates \  
g++ \  
make \  
openssl \  
pcre-dev \  
wget \  
&& wget -O /tmp/astyle_${VERSION}_linux.tar.gz
https://downloads.sourceforge.net/project/astyle/astyle/astyle%20${VERSION}/astyle_${VERSION}_linux.tar.gz
\  
&& tar -zxf /tmp/astyle_${VERSION}_linux.tar.gz -C /tmp \  
&& cd /tmp/astyle/build/gcc \  
&& make release \  
&& USER=root make install \  
&& rm /tmp/astyle_${VERSION}_linux.tar.gz \  
&& rm -rf /tmp/astyle \  
&& apk del build-dependencies  
  
RUN apk add --no-cache libstdc++  
  
ARG USER=user  
ARG UID=1000  
ENV USER $USER  
RUN mkdir /home/$USER \  
&& addgroup -g $UID -S $USER \  
&& adduser -u $UID -D -S -G $USER $USER \  
&& chown -R $USER:$USER /home/$USER  
  
USER $USER  
VOLUME /data  
WORKDIR /data  
  
CMD []  
ENTRYPOINT ["astyle"]  

