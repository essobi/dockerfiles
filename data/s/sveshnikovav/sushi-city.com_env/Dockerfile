FROM postgres:9.6  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "Europe/Moscow" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="ru_RU.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=ru_RU.UTF-8  
RUN apt-get update && apt-get upgrade -y && apt-get install -y --fix-missing
postgresql-contrib postgis postgresql-9.6-postgis-2.3  
  

