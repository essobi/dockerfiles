FROM tutum/apache-php  
ADD . /web-reserved  
WORKDIR /web-reserved  
RUN rm -fr /app && ln -s /web-reserved/public /app  
ENV ALLOW_OVERRIDE **TRUE**  

