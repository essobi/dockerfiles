FROM alpine:3.5  
  
MAINTAINER Pawel Mazurek  
  
ENV VERSION "v2.2.10"  
ENV FOLDER "swagger-ui-2.2.10"  
ENV API_URL "http://petstore.swagger.io/v2/swagger.json"  
ENV API_URLS [{name:\"COOD\", url:\"http://swaggerui-dop-
tools.kermit.itn.intraorange/json/swaggerCood.json\"},{name:\"VELOCITY\",
url:\"http://swaggerui-dop-tools.kermit.itn.intraorange/json/velocity.json\"},
{name:\"NRA \- Resource Inventory\", url:\"http://swaggerui-dop-
tools.kermit.itn.intraorange/json/ResourceInventoryManagement-
API-v0.3.0.yaml\"}]  
  
  
ENV OAUTH_CLIENT_ID "**None**"  
ENV OAUTH_CLIENT_SECRET "**None**"  
ENV OAUTH_REALM "**None**"  
ENV OAUTH_APP_NAME "**None**"  
ENV OAUTH_ADDITIONAL_PARAMS "**None**"  
ENV SWAGGER_JSON "/app/swagger.json"  
ENV PORT 8080  
ENV BASE_URL ""  
  
RUN apk add --update nginx  
RUN mkdir -p /run/nginx  
  
COPY nginx.conf /etc/nginx/  
ADD ./json/* /usr/share/nginx/html/json/  
# copy swagger files to the `/js` folder  
ADD ./dist/* /usr/share/nginx/html/  
ADD ./docker-run.sh /usr/share/nginx/  
RUN chgrp -R 0 /var/run  
RUN chmod -R g+rwX /var/run  
RUN chgrp -R 0 /usr/share/nginx/html  
RUN chmod -R g+rwX /usr/share/nginx/html  
RUN chgrp -R 0 /etc/nginx  
RUN chmod -R g+rwX /etc/nginx  
RUN chgrp -R 0 /var/lib/nginx  
RUN chmod -R g+rwX /var/lib/nginx  
RUN chgrp -R 0 /var/lib/nginx/logs  
RUN chmod -R g+rwX /var/lib/nginx/logs  
RUN chgrp -R 0 /run/nginx  
RUN chmod -R g+rwX /run/nginx  
RUN chgrp -R 0 usr/share/nginx  
RUN chmod -R g+rwX /usr/share/nginx  
  
EXPOSE 8080  
USER 555  
  
CMD ["sh", "/usr/share/nginx/docker-run.sh"]  

