FROM tutum/apache-php  
RUN apt-get update && apt-get install -yq git && rm -rf /var/lib/apt/lists/*  
RUN rm -fr /app  
ADD . /app  
RUN cd /app/application/ && composer install

