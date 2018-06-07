FROM mhart/alpine-node:6.11  
ENV ADDITIONAL_PKGS="make g++ python nasm autoconf automake zlib-dev git
tzdata"  
WORKDIR /var/www/feschibal  
COPY . /var/www/feschibal/  
  
RUN npm update -g npm && \  
npm install -g grunt-cli  
  
RUN apk add --no-cache ${ADDITIONAL_PKGS} && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
npm install --unsafe-perm && \  
grunt build  
  
EXPOSE 9000 35729  
ENV NODE_ENV="development"  
CMD ["grunt", "serve:express"]  

