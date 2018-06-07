FROM debian:stretch-slim  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install requirements  
RUN apt-get update -yqq \  
&& apt-get install wget gnupg -yqq \  
&& echo "deb http://repo.yandex.ru/yandex-disk/deb/ stable main" | tee -a
/etc/apt/sources.list.d/yandex.list > /dev/null \  
&& wget http://repo.yandex.ru/yandex-disk/YANDEX-DISK-KEY.GPG -O- | apt-key
add - \  
&& apt-get update \  
&& apt-get install -y yandex-disk \  
&& apt-get clean \  
&& rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/lib/apt/lists/*  
  
RUN mkdir /sync  
  
# Folder to mount  
VOLUME ["/sync"]  
  
# Copy start script  
COPY start.sh /  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

