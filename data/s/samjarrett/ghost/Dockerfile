FROM ghost:1-alpine  
  
ENV url="http://localhost" \  
database__client="mysql" \  
database__connection__host="db"  
ENV DUMB_INIT_VERSION "1.2.0"  
RUN set -xe && \  
apk add --no-cache --virtual .initdeps curl && \  
curl -sSLo /usr/local/bin/dumb-init \  
https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
chmod +x /usr/local/bin/dumb-init && \  
apk del --no-cache .initdeps && \  
true  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "docker-entrypoint.sh"]  
CMD ["node", "current/index.js"]  
  
USER node  

