FROM ubuntu:16.04  
ENV PORT=80  
ENV PRODUCTION=1  
RUN apt-get update  
RUN apt-get install -y --force-yes nodejs nodejs-legacy npm mongodb  
RUN npm install -g gulp  
RUN npm install helmet --save  
  
RUN mkdir -p /root/mongo-sites-api  
COPY package.json /root/mongo-sites-api/package.json  
  
WORKDIR /root/mongo-sites-api  
RUN bash -c 'npm update || echo'  
COPY . /root/mongo-sites-api  
RUN gulp  
  
CMD bash /root/mongo-sites-api/run_app.sh  

