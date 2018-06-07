FROM php:alpine  
  
# Install python  
RUN apk --update add \  
python3 \  
curl && \  
rm /var/cache/apk/*  
RUN ln -sf /usr/bin/python3 /usr/bin/python  
  
COPY app /app  
  
RUN adduser -u 5000 app -D  
RUN chown -R app:app /app  
  
USER app  
  
WORKDIR /app  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN ./composer.phar install  
RUN rm /app/composer.phar  
  
WORKDIR /code  
  
CMD python /app/run.py  

