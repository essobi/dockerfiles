FROM prima/elixir-official:1.6.5  
# Timezone data  
RUN apt-get update && \  
apt-get install -qqy tzdata mysql-client && \  
apt-get clean && \  
cp /usr/share/zoneinfo/Europe/Rome /etc/localtime && \  
echo "Europe/Rome" > /etc/timezone && \  
date  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

