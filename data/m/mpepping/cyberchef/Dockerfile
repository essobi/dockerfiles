FROM alpine:3.5  
LABEL maintainer 'Martijn Pepping <martijn.pepping@automiq.nl>'  
  
RUN addgroup cyberchef -S && \  
adduser cyberchef -G cyberchef -S && \  
apk update && \  
apk add nodejs curl git && \  
rm -rf /var/cache/apk/* && \  
npm install -g grunt-cli && \  
npm install -g http-server  
  
RUN cd /srv && \  
curl -L https://github.com/gchq/CyberChef/archive/v7.11.1.tar.gz | tar zxv &&
\  
cd CyberChef-7.11.1 && \  
rm -rf .git && \  
npm install && \  
npm cache rm && \  
chown -R cyberchef:cyberchef /srv/CyberChef-7.11.1 && \  
grunt prod  
  
WORKDIR /srv/CyberChef-7.11.1/build/prod  
USER cyberchef  
ENTRYPOINT ["http-server", "-p", "8000"]  

