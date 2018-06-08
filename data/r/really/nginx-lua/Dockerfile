FROM alpine  
  
RUN apk add --no-cache nginx nginx-mod-http-lua nginx-mod-http-lua-upstream
nginx-mod-devel-kit && \  
mkdir -p /run/nginx  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

