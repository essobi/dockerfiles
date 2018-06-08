FROM alpine  
  
RUN apk add nodejs yarn paxctl --no-cache  
RUN paxctl -cm `which node`  
  
WORKDIR /app  
  
ADD *.js ./  
ADD *.json ./  
ADD public ./public  
  
RUN chmod 755 .  
RUN chmod 644 ./*  
RUN chmod 755 ./public  
RUN chmod 644 ./public/*  
  
RUN yarn install  
  
CMD [ "node", "index.js" ]

