FROM ubuntu  
  
LABEL maintainer="Oliger Timothee"  
  
RUN apt-get update && apt-get install -y apt-utils dialog openssh-client curl
git &&\  
curl -sL https://deb.nodesource.com/setup_8.x | bash - &&\  
apt-get install -y nodejs build-essential  
  
RUN npm i -g pm2  
  
ADD ./app /app  
  
ENTRYPOINT cd /app && pm2 start app.js && while true; do sleep 1000; done  
  
EXPOSE 8080  

