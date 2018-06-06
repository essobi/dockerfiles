FROM prima/elixir-official:1.6.5  
  
COPY files/apt/99defaultrelease /etc/apt/apt.conf.d/99defaultrelease  
COPY files/apt/stable.list /etc/apt/sources.list.d/stable.list  
COPY files/apt/testing.list /etc/apt/sources.list.d/testing.list  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.6" >
"/etc/apt/sources.list.d/postgresql.list" && \  
curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add \-
&& \  
apt-get update && \  
apt-get install -qqy postgresql-client-9.6 pdftk && \  
apt-get -t testing install -qqy ghostscript imagemagick && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

