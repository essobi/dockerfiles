FROM php:5-cli  
  
RUN apt-get update -qq && apt-get install -y git  
  
WORKDIR /root  
  
RUN git clone https://github.com/stersin/MagentoTarToConnect.git  
ADD build-package.sh .  
  
ENTRYPOINT ["./build-package.sh"]  

