FROM ubuntu  
RUN apt-get update  
RUN apt-get -y install git  
RUN apt-get -y install composer  
RUN apt-get -y install php-mbstring  
RUN apt-get -y install php-dom  
RUN git clone https://github.com/Varajey/TestCircleCI.git  
RUN composer install --working-dir=TestCircleCI  
RUN apt-get -y install docker-compose

