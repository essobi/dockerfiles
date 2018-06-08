FROM prima/elixir-official:1.6.5  
# Timezone data ed ssh per sftp  
RUN apt-get update && \  
apt-get install -y tzdata erlang-ssh openssh-client expect mysql-client && \  
rm -rf /var/cache/apk/* && \  
cp /usr/share/zoneinfo/Europe/Rome /etc/localtime && \  
echo "Europe/Rome" > /etc/timezone && \  
date  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

