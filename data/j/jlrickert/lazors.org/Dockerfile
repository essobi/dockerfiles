FROM ubuntu  
RUN apt-get update && \  
apt-get install -y \  
python3 \  
python3-pip \  
redis-server  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY . /game  
WORKDIR /game  
RUN pip3 install -r requirements.txt  
EXPOSE 8000  
ENV APP_ENV DEVELOPMENT  
ENV APP_ALLOWED_HOST "0.0.0.0"  
ENV APP_SECRET_KEY "cnwu)=j8md5-*47as)zxd)z3r0-+y51agif9vvwp3%6e#$%r@9"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["runserver", "0.0.0.0:8000"]  

