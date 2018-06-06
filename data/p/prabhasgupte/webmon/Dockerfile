FROM php:7.0-cli  
  
LABEL maintainer="Prabhas Gupte <prabhas.gupte@gmail.com>"  
LABEL "webmon-version"="1.3.0"  
  
COPY . /app  
WORKDIR /app  
CMD [ "php", "./webmon.php", "-i/app/store/seeds.txt" ]  

