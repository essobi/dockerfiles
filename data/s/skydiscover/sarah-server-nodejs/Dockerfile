FROM cusspvz/node  
  
WORKDIR /home/pi/SARAH-Server-NodeJS  
  
RUN apk --update --no-cache add \  
build-base \  
openssl \  
python \  
sudo \  
tar \  
tzdata && \  
wget https://github.com/JpEncausse/SARAH-Server-NodeJS/archive/master.tar.gz
-O - \  
| tar -xz --strip-components=1 && \  
cd server/app && \  
npm install && \  
sed 's/app.js &/app.js/' -i /home/pi/SARAH-Server-NodeJS/sarah-server.sh && \  
chmod +x /home/pi/SARAH-Server-NodeJS/sarah-server.sh && \  
apk del build-base openssl python tar  
  
ENV TZ Europe/Paris  
  
EXPOSE 8080 8888  
VOLUME /home/pi/SARAH-Server-NodeJS  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["sarah-server.sh", "start"]  
  

