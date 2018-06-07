# vim: set ft=dockerfile:  
FROM mhart/alpine-node:0.12  
# Author with no obligation to maintain  
MAINTAINER Paul Tötterman <paul.totterman@iki.fi>  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh \  
&& apk --no-cache add curl su-exec \  
&& addgroup -S -g 333 etherpad \  
&& adduser -S -u 333 -G etherpad etherpad \  
&& curl -sLo /etherpad.tar.gz https://github.com/ether/etherpad-
lite/archive/1.5.7.tar.gz \  
&& mkdir /opt \  
&& tar -xz -C /opt -f /etherpad.tar.gz \  
&& mv /opt/etherpad-lite-1.5.7 /opt/etherpad \  
&& rm -f /etherpad.tar.gz \  
&& sed -i -e "93 s,grep.*,grep -E -o 'v[0-9]\\.[0-9](\\.[0-9])?'),"
/opt/etherpad/bin/installDeps.sh \  
&& sed -i -e '96 s,if.*,if [ "${VERSION#v}" = "$NEEDED_VERSION" ]; then,'
/opt/etherpad/bin/installDeps.sh \  
&& /opt/etherpad/bin/installDeps.sh \  
&& rm -rf /tmp/*  
COPY settings.json /opt/etherpad/settings.json  
  
EXPOSE 9001  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/opt/etherpad/bin/run.sh"]  

