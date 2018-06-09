FROM nginx:alpine  
  
# Environments  
ENV TIMEZONE Etc/UTC  
  
RUN apk update && \  
apk add --update tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk add --update \  
ca-certificates \  
fuse \  
&& \  
  
# Cleaning up  
mkdir /www && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/nginx-site /etc/nginx/sites-enabled/default  
  
# Set Workdir  
WORKDIR /www  
  
# Expose volumes  
VOLUME ["/www"]  
  
# Expose ports  
EXPOSE 80  

