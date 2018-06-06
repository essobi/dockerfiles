FROM alpine:edge  
  
WORKDIR /srv  
  
COPY package.json .  
COPY yarn.lock .  
  
RUN \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk add --no-cache nodejs-current yarn vips-dev fftw-dev make g++ python && \  
yarn && \  
apk del make g++ python && \  
rm -rf /var/cache/apk/*  
  
COPY src src  
COPY test test  
  
# Expose webapp port  
EXPOSE 8080  
ENTRYPOINT ["yarn"]  
CMD ["start"]  

