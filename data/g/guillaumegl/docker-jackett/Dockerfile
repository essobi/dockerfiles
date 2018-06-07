FROM gliderlabs/alpine:latest  
  
MAINTAINER guillaumeGL <guillaume.lebeau@outlook.com>  
  
ENV VERSION 0.6.8  
# Update the package list  
RUN apk update  
  
# Install all needed packages. Tar+Bzip2 to uncompress Jackett archive and
libcurl+Mono as dependencies to Jackett  
RUN apk add curl tar bzip2  
RUN apk add mono --update-cache --repository
http://alpine.gliderlabs.com/alpine/edge/testing/ --allow-untrusted  
  
RUN curl -L
https://jackett.net/Download/v${VERSION}/Jackett.Mono.v${VERSION}.tar.bz2 -o
/tmp/jackett.tar.bz2  
RUN mkdir -p /tmp/jackett  
RUN tar -jxvf /tmp/jackett.tar.bz2 -C /tmp/jackett  
RUN mkdir -p /data/app  
RUN mv /tmp/jackett/Jackett /data/app  
RUN chown -R nobody:users /data/app  
RUN mkdir -p /data/config  
RUN chown -R nobody:users /data/config  
RUN ln -s /data/config /usr/share/Jackett  
  
EXPOSE 9117  
VOLUME /data/config  
VOLUME /data/app  
  
ADD start.sh /  
RUN chmod +x /start.sh  
  
WORKDIR /data/app/Jackett  
  
ENTRYPOINT ["mono", "JackettConsole.exe"]  

