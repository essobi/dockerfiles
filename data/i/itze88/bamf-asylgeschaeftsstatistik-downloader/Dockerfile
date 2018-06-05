FROM java:8  
COPY . /usr/src/myapp  
WORKDIR /usr/src/myapp  
  
RUN apt-get update \  
&& apt-get install -y wget php5 php5-cli  
  
CMD ["php", "./crawler.php"]  

