FROM grin/abraham  
LABEL maintainer="And Grin <a@grin.ly>"  
  
# download the oauth2_proxy v.2.2  
ARG
OAUTH_URL=https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-
amd64.go1.8.1.tar.gz  
ARG OAUTH_LOC=/proxy  
  
ADD ${OAUTH_URL} /oauth.tar.gz  
  
RUN mkdir -p $OAUTH_LOC && tar -xzf /oauth.tar.gz --strip-components 1 -C
$OAUTH_LOC  
  
# copy configs etc  
COPY ./container/root /  
WORKDIR /app/  
  
RUN chmod u+x startup2.sh  
  
CMD ["bash", "-C", "/app/startup2.sh"]  

