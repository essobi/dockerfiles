FROM nginx:1.9  
ENV SWAGGER_UI_VERSION 2.1.2-M2  
ENV URL **None**  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -L https://github.com/swagger-api/swagger-
ui/archive/v${SWAGGER_UI_VERSION}.tar.gz | tar -zxv -C /tmp \  
&& cp -R /tmp/swagger-ui-${SWAGGER_UI_VERSION}/dist/* /usr/share/nginx/html \  
&& rm -rf /tmp/*  
  
COPY run.sh /run.sh  
  
CMD ["/run.sh"]  

