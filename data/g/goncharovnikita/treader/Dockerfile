FROM mhart/alpine-node:8.9.4 as builder  
  
WORKDIR /app  
  
COPY . /app  
  
RUN npm install  
  
RUN npm run build  
  
FROM abiosoft/caddy  
  
COPY \--from=builder /app/dist /app  
  
COPY Caddyfile /etc/Caddyfile  
  
EXPOSE 80 443 2015  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]

