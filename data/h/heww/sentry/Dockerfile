FROM library/sentry:8.15.0-onbuild  
  
RUN apt-get update && apt-get install -y --no-install-recommends curl \  
&& curl -SL https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz
| tar xzvf - -C /usr/local/bin \  
&& chmod +x /usr/local/bin/forego \  
&& apt-get purge -y --auto-remove curl \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["./run"]  

