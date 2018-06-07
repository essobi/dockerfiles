FROM qinyuguang/yafbase:latest  
  
VOLUME ["/www/dataflow", "/home/logs/project/dataflow",
"/home/logs/php/dataflow"]  
  
COPY ./ /www/dataflow/  
COPY ./conf/online/php.ini /usr/local/etc/php/php.ini  
COPY ./conf/online/fpm.conf /usr/local/etc/php-fpm.d/dataflow.conf  
  
WORKDIR /www/dataflow  
  
CMD /www/dataflow/start.sh  
  

