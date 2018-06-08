FROM node:6-alpine  
COPY . /padlock  
WORKDIR /padlock  
RUN apk add --no-cache curl git \  
&& npm install -g gulp bower \  
&& npm install \  
&& bower install --allow-root \  
&& gulp stylus \  
&& npm uninstall gulp bower \  
&& rm -rf node_modules \  
&& curl -sSL -o ./serve
https://github.com/gesellix/spark/releases/download/1.5/spark_linux_amd64 \  
&& chmod +x ./serve \  
&& adduser -S padlock \  
&& chown -R padlock /padlock \  
&& apk del --no-cache git curl  
USER padlock  
EXPOSE 8080  
CMD [ "./serve", "." ]  

