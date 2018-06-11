FROM ubuntu:16.04  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get -y install \  
wget \  
sudo \  
vim \  
&& rm -r /var/lib/apt/lists/*  
  
RUN echo "deb http://repo.yandex.ru/yandex-disk/deb/ stable main" | tee -a
/etc/apt/sources.list.d/yandex.list > /dev/null && wget
http://repo.yandex.ru/yandex-disk/YANDEX-DISK-KEY.GPG -O- | apt-key add - &&
apt-get update && apt-get install -y yandex-disk && rm -r /var/lib/apt/lists/*  
  
COPY init.sh /init.sh  
  
RUN chmod +x /init.sh && mkdir /mnt/yandex.disk  
  
ENV YANDEX_USER "USERNAME@yandex.ru"  
ENV YANDEX_PASSWORD "PASSWORD"  
ENV FOLDER = "/mnt/yandex.disk"  
  
CMD ["/init.sh"]

