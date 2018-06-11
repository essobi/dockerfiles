FROM webvariants/php-sally-node:5.6  
  
RUN apt-get update && apt-get install -y libxml2-dev && rm -r
/var/lib/apt/lists/*  
  
RUN docker-php-ext-install mysqli soap  
  
RUN echo "always_populate_raw_post_data=-1" >
/usr/local/etc/php/conf.d/typo3.ini \  
&& echo "max_input_vars=1500" >> /usr/local/etc/php/conf.d/typo3.ini \  
&& echo "max_execution_time=240" >> /usr/local/etc/php/conf.d/typo3.ini  

