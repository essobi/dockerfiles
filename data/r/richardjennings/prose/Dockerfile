FROM nginx:alpine  
  
MAINTAINER Richard Jennings <richardjennings@gmail.com>  
  
ENV PROSE_VERSION="1.1.21"  
  
RUN apk add --no-cache --virtual .build-deps curl gcc g++ make python nodejs
musl-dev git \  
&& curl https://codeload.github.com/prose/prose/tar.gz/v${PROSE_VERSION} -o
/tmp/prose.tar.gz \  
&& tar -xvzf /tmp/prose.tar.gz -C /tmp && mv /tmp/prose-${PROSE_VERSION}
/build && rm /tmp/prose.tar.gz \  
&& npm install -g gulp \  
&& cd /build \  
&& echo
'{api:"https://api.github.com",site:"https://github.com",clientId:"%GITHUB_CLIENT_ID%",gatekeeperUrl:""}'
> oauth.json \  
&& npm install && gulp \  
&& npm uninstall \  
&& apk del .build-deps \  
&& mkdir /app \  
&& cp -a img fonts index.html style-rtl.css locale.js oauth.json translations
/app \  
&& cp -R /build/dist /app \  
&& chown -R nginx:nginx /app \  
&& rm -rf /build  
  
WORKDIR /app  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY entrypoint.sh /app  
RUN chmod +x /app/entrypoint.sh  
  
CMD ["/app/entrypoint.sh"]

