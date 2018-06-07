FROM heres/alpine-supervisord  
MAINTAINER "Łukasz Kaczynski" <heres@devsoft.pl>  
ENV PATH /usr/local/bin:$PATH  
  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN mkdir -p /app  
  
ADD . /app  
WORKDIR /app  
  
RUN pip3 install -r /app/requirements.txt  
EXPOSE 8000  

