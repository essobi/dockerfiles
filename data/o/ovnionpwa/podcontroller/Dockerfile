FROM node:alpine  
ADD . /podcontroller/  
WORKDIR /podcontroller/  
RUN apk update && apk add curl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
RUN mv ./kubectl /usr/local/bin/kubectl  
RUN npm install  
CMD ["sh","run.sh"]  

