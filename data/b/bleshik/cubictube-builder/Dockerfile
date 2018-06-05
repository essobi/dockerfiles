FROM bleshik/scala:2.11.5  
COPY ./ /src  
RUN apt-get update -y && apt-get install -y openssh-client npm python-pip  
RUN pip install awscli  
RUN npm install npm@latest -g && npm install -g n && n 6.10.3 && n use 6.10.3  
RUN npm install -g yarn@1.3.2  
RUN cd /src/backend/api && yarn install && cd /src/web-app && yarn install &&
rm -rf /src  

