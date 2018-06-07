FROM nginx:1.12.0-alpine  
  
LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"  
LABEL creator "Mikael Robert <mikaelrob@gmail.com>"  
  
ENV MODE=default \  
NGX_DEFAULT=true \  
NGX_CFG=  
  
RUN apk add --update --no-cache --virtual .build-deps curl && \  
curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-
linux -o /usr/local/bin/dkconf && \  
chmod +x /usr/local/bin/dkconf && \  
apk del .build-deps  
  
COPY ["templates", "/usr/local/etc/nginx/templates"]  
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]  
  
CMD ["/usr/local/bin/docker-entrypoint.sh"]  

