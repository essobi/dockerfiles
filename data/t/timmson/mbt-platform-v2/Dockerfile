FROM timmson/mbt-platform-v2:platform  
LABEL maintaner="Krotov Artem <timmson666@mail.ru>"  
  
RUN apt update && apt install -y mongodb-server && \  
sed -i "s|bind_ip = 127.0.0.1|bind_ip = 0.0.0.0 |g" /etc/mongodb.conf && \  
mkdir -p /data/db /data/configdb  
  
VOLUME /data/db /data/configdb  
  
CMD ["mongod"]

