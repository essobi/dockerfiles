FROM alpine:3.6  
  
# from https://github.com/aptible/supercronic/releases  
ENV
SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.2/supercronic-
linux-amd64 \  
SUPERCRONIC=supercronic-linux-amd64 \  
SUPERCRONIC_SHA1SUM=cdfde14f50a171cbfc35a3a10429e2ab0709afe0  
  
ENTRYPOINT [ "/sbin/tini", "--" ]  
  
# install dependencies  
RUN apk add \--no-cache \  
ca-certificates \  
curl \  
tini \  
  
# install supercronic  
# (from https://github.com/aptible/supercronic/releases)  
&& curl -fsSLO "$SUPERCRONIC_URL" \  
&& echo "${SUPERCRONIC_SHA1SUM} ${SUPERCRONIC}" | sha1sum -c - \  
&& chmod +x "$SUPERCRONIC" \  
&& mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \  
&& ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic \  
  
# clean up dependencies  
&& apk del --purge \  
ca-certificates \  
curl \  
&& rm -rf /var/cache/apk/  
  
ADD crontab.sample /etc/crontab  
  
CMD [ "/usr/local/bin/supercronic", "/etc/crontab" ]  
  

