FROM debian:jessie  
MAINTAINER Jan Kurwahn <jan.kurwahn@gmail.com>  
  
ARG RELEASE=0.3.0  
ENV RELEASE ${RELEASE}  
  
ARG NAME=gophish-v0.3-linux-64bit  
ENV NAME ${NAME}  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
unzip \  
ca-certificates \  
wget && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /opt  
RUN wget -nv
https://github.com/gophish/gophish/releases/download/v$RELEASE/$NAME.zip && \  
unzip $NAME.zip && \  
rm -f $NAME.zip  
  
WORKDIR /opt/$NAME  
RUN sed -i "s|127.0.0.1|0.0.0.0|g" config.json && \  
chmod +x gophish  
  
EXPOSE 3333 80  
ENTRYPOINT ["./gophish"]

