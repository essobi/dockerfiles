FROM alpine:3.6  
MAINTAINER "Frank Wolf <FrankWolf@gmx.de>"  
LABEL Maintainer="Frank Wolf <FrankWolf@gmx.de>" \  
Name="lcov-to-cobertura-xml" \  
Version=0.1.0  
  
RUN apk add --no-cache --virtual build-dependencies \  
ca-certificates \  
openssl \  
wget \  
&& wget -O lcov_cobertura.py https://raw.github.com/eriwen/lcov-to-cobertura-
xml/master/lcov_cobertura/lcov_cobertura.py \  
&& apk del build-dependencies \  
&& apk add --no-cache python  
  
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
  
CMD ["coverage.info"]  
ENTRYPOINT ["/usr/bin/python", "/lcov_cobertura.py"]  

