FROM kuzzleio/bo-base:alpine  
MAINTAINER Kuzzle <support@kuzzle.io>  
  
ADD /scripts /  
RUN set -ex && \  
chmod 755 /*.sh && \  
curl -Ls https://github.com/kuzzleio/kuzzle-
containers/releases/download/dockerized-phantomjs-2.1.1/dockerized-
phantomjs.tar.gz \  
| tar xz -C / && \  
apk update && \  
apk add --no-cache openjdk8-jre dbus firefox-esr xvfb && \  
dbus-uuidgen > /var/lib/dbus/machine-id && \  
echo "done"  
  
ENV TERM=xterm-color  
  
CMD ["/run-test.sh"]  

