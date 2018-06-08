FROM alpine:3.7  
RUN set -ex \  
&& apk update \  
&& apk upgrade \  
&& apk add \  
nodejs-npm \  
&& npm i -g raml2html@7.1.0 \  
&& npm cache clean --force \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["raml2html"]  
  
CMD ["-h"]  

