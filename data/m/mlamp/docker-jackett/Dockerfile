FROM alpine:3.5  
MAINTAINER mlamp  
  
ENV VERSION 0.7.1272  
# Update the package list  
RUN apk update  
  
# Install all needed packages. Tar+Bzip2 to uncompress Jackett archive and
libcurl+Mono as dependencies to Jackett  
RUN apk add curl tar bzip2  
RUN apk add mono --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
RUN curl -L
http://github.com/Jackett/Jackett/releases/download/v${VERSION}/Jackett.Binaries.Mono.tar.gz
-o /tmp/jackett.tar.gz  
RUN mkdir -p /tmp/jackett  
RUN tar xvfz /tmp/jackett.tar.gz -C /tmp/jackett  
RUN mkdir -p /data/app  
RUN mv /tmp/jackett/Jackett/* /data/app  
RUN chown -R nobody:nogroup /data/app  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir -p /data/config  
RUN chown -R nobody:nogroup /data/config  
RUN ln -s /data/config /usr/share/Jackett  
  
EXPOSE 9117  
VOLUME /data/config  
VOLUME /data/app  
  
WORKDIR /data/app  
  
ENTRYPOINT ["mono", "JackettConsole.exe"]  

