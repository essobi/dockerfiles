FROM prima/elixir-official:1.6.5  
  
RUN apt-get update && \  
apt-get install -qqy erlang-ssh openssh-client mysql-client unzip libtext-
iconv-perl && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

