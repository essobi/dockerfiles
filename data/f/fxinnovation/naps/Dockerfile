FROM openresty/openresty:xenial  
  
ENV PORT=8000 \  
WORKER_CONNECTIONS=128 \  
RESOLVER=host \  
CONFD_VERSION=0.11.0 \  
LUA_RESTY_HTTP_VERSION=0.10-0 \  
OIC_REDIRECT_URI_PATH=login \  
OIC_DISCOVERY="https://example.com" \  
OIC_CLIENT_ID=foo \  
OIC_CLIENT_SECRET=bar \  
OIC_AUTHORIZATION_PARAMS="hd=\"example.com\"" \  
OIC_SCOPE="openid email profile" \  
OIC_REDIRECT_URI_SCHEME="https" \  
OIC_LOGOUT_PATH="logout" \  
OIC_REDIRECT_AFTER_LOGOUT_URI="/" \  
OIC_USER_HEADER="X-USER" \  
OIC_DOMAIN="example.com" \  
SESSION_STORAGE="cookie" \  
SESSION_SECRET="pleasechangethisbecauseitisimportant" \  
PROXY_PASS="http://example.com"  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ADD ./resources /resources  
  
RUN /resources/build && rm -rf /resources  
  
LABEL "maintainer"="cloudsquad@fxinnovation.com" \  
"org.label-schema.name"="naps" \  
"org.label-schema.base-image.name"="openresty/openresty" \  
"org.label-schema.base-image.version"="xenial" \  
"org.label-schema.description"="NGINX Auth Proxy System" \  
"org.label-schema.url"="https://bitbucket.org/fxadmin/public-common-docker-
naps" \  
"org.label-schema.vcs-url"="https://bitbucket.org/fxadmin/public-common-
docker-naps" \  
"org.label-schema.vendor"="FXinnovation" \  
"org.label-schema.schema-version"="1.0.0-rc.1" \  
"org.label-schema.applications.resty.version"=$RESTY_VERSION \  
"org.label-schema.applications.resty_ssl.version"=$RESTY_SSL_VERSION \  
"org.label-schema.applications.resty_pcre.version"=$RESTY_PCRE_VERSION \  
"org.label-schema.vcs-ref"=$VCS_REF \  
"org.label-schema.version"=$VERSION \  
"org.label-schema.build-date"=$BUILD_DATE \  
"org.label-schema.usage"="https://bitbucket.org/fxadmin/public-common-docker-
naps"  

