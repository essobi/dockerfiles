FROM mysql:latest  
  
RUN apt-get update && \  
apt-get install -y locales && \  
rm -rf /var/lib/apt/lists/* && \  
echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
  
ENV TZ Asia/Tokyo  
RUN apt-get install -y tzdata && \  
rm -rf /var/lib/apt/lists/* && \  
echo "${TZ}" > /etc/timezone && \  
rm /etc/localtime && \  
ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata  
  
RUN { \  
echo '[mysqld]'; \  
echo 'character-set-server=utf8mb4'; \  
echo 'collation-server=utf8mb4_bin'; \  
echo '[client]'; \  
echo 'default-character-set=utf8mb4'; \  
} > /etc/mysql/conf.d/charset.cnf

