FROM node:8-alpine  
  
RUN apk --no-cache add \  
bash \  
build-base \  
git \  
openssh-client \  
python \  
rsync \  
&& \  
npm install --silent -g gulp bower && \  
sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd  

