FROM nginx:alpine  
  
MAINTAINER devicehive  
  
RUN mkdir -p /opt/devicehive/admin  
  
ADD admin-start.sh /opt/devicehive/  
  
RUN apk update && apk upgrade && \  
apk add git && \  
git clone https://github.com/devicehive/devicehive-admin-console.git
/tmp/devicehive-admin-console && \  
cp -r /tmp/devicehive-admin-console/* /opt/devicehive/admin/ && \  
sed -i -e 's/restEndpoint.*/restEndpoint: location.origin +
\"\/api\/rest\"\,/' /opt/devicehive/admin/scripts/config.js  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
WORKDIR /opt/devicehive/  
  
ENTRYPOINT ["/bin/sh"]  
  
CMD ["./admin-start.sh"]  

