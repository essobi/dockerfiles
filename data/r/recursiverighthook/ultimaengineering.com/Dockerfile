FROM ubuntu:14.04  
RUN apt-get update && apt-get install software-properties-common python-
software-properties curl -y  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install nodejs  
WORKDIR /app/webapp  
COPY . /app/webapp  
RUN npm install && npm run build && npm install -g serve  
EXPOSE 5000  
ENTRYPOINT serve -s build

