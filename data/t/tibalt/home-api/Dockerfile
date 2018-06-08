FROM tibalt/alpine-node:rpi  
  
RUN [ "cross-build-start" ]  
  
RUN \  
apk add --no-cache make gcc g++ python linux-headers udev && \  
npm i serialport --build-from-source  
  
WORKDIR /app  
  
ADD https://api.github.com/repos/darkwebdev/home-api/git/refs/heads/master
version.json  
  
RUN \  
git clone \--depth=1 -b master https://github.com/darkwebdev/home-api.git && \  
cd home-api && \  
npm i  
  
RUN \  
chown -R app:users /app/home-api && \  
usermod -G dialout app  
  
RUN [ "cross-build-end" ]  
  
COPY ./app /app  
  
EXPOSE 8080  
USER app  
  
ENTRYPOINT ["sh", "/app/entry.sh"]  

