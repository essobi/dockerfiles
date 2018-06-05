FROM elixir:1.2.5  
ENV PHOENIX_VERSION "1.1.4"  
RUN \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
apt-get clean && \  
cd /var/lib/apt/lists && rm -fr *Release* *Sources* *Packages* && \  
truncate -s 0 /var/log/*log  
  
RUN \  
mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phoenix_new-$PHOENIX_VERSION.ez  
  
CMD ["iex"]  

