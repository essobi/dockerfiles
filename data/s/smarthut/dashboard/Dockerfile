FROM node:latest as builder  
COPY . .  
RUN npm install  
RUN npm run build  
  
FROM alpine:latest  
RUN apk add --no-cache curl bash \  
&& curl -fsSL https://getcaddy.com | bash -s personal  
COPY \--from=builder /build /www  
COPY Caddyfile /etc/Caddyfile  
EXPOSE 80 443 2015  
ENTRYPOINT ["caddy"]  
CMD ["--conf", "/etc/Caddyfile"]  

