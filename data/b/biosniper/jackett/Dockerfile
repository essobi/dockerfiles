FROM alpine:latest  
  
WORKDIR /opt  
  
#Install dependencies and install mono  
RUN apk add --update wget tar bzip2 curl-dev && apk add mono --update-cache
--repository http://nl.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
&& rm -Rfv /var/cache/apk/*  
  
#Create group and user  
RUN addgroup -S jackett && adduser -s /bin/false -h /usr/share/Jackett -G
jackett -S jackett && mkdir -p /usr/share/Jackett && chown -R jackett:
/usr/share/Jackett  
  
#Wget Jackett decompress then cleanup  
RUN wget --no-check-certificate -q
https://github.com/Jackett/Jackett/releases/download/v0.7.181/Jackett.Binaries.Mono.tar.gz
&& tar -zxf Jackett.Binaries.Mono.tar.gz && rm -v
/opt/Jackett.Binaries.Mono.tar.gz  
  
#Set the owner  
RUN chown -R jackett: /opt/Jackett  
  
#Map /config to host defined config path (used to store configuration from
supervisor)  
VOLUME /config  
  
#Map /root/.config/Jackett to host defined config path (used to store
configuration from Jackett)  
VOLUME /root/.config/Jackett  
  
#Expose port for http  
EXPOSE 9117  
#Run  
ENTRYPOINT ["/usr/bin/mono", "--debug", "/opt/Jackett/JackettConsole.exe"]  
CMD ["-x", "true"]  

