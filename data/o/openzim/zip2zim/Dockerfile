FROM openzim/zimwriterfs:latest  
  
RUN apt-get update  
  
# Install npm & nodejs  
RUN apt-get install -y python make gcc build-essential openssl libssl-dev pkg-
config git  
RUN wget https://nodejs.org/dist/v6.10.3/node-v6.10.3.tar.gz  
RUN tar xvf node-v6.10.3.tar.gz  
RUN cd node-v6.10.3 && ./configure  
RUN cd node-v6.10.3 && make all install  
  
# Local Development  
#COPY ./ /app  
RUN \  
git clone https://github.com/openzim/zip2zim.git /app && \  
cd /app && \  
npm i  
RUN cd /app && npm run build  
  
WORKDIR /app  
  
EXPOSE 8000  
ENTRYPOINT ["node"]  
CMD ["./node_modules/.bin/pm2-docker", "build/index.js"]

