FROM nginx:alpine  
  
# Copy app files  
COPY build /usr/share/nginx/html  
  
# Install SPA-friendly config  
COPY nginx/default.conf /etc/nginx/conf.d/  
  
# Install JQ to work with JSON configs  
RUN apk add --no-cache jq  
  
#Configure and start the app  
WORKDIR /usr/share/nginx/html  
  
CMD /bin/ash -c "echo -n 'window.__CONFIG=' > config.js && jq -ncM
'{apiBaseUrl: env.API_BASE_URL}' >> config.js && cat config.js && nginx -g
'daemon off;'"  

