FROM debian:jessie  
  
ENV
HEROKU_TAR_SHA=03b6eea4e17249ee3713d28013c2757fd746a0bf8fd4eb531940e7781da8a8a9  
  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y --no-install-recommends git wget ca-
certificates \  
&& wget http://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz
\  
&& echo "Downloaded archive SHA: $( sha256sum heroku-linux-amd64.tar.gz | cut
-d' ' -f1 )" \  
&& [ $( sha256sum heroku-linux-amd64.tar.gz | cut -d" " -f1 ) =
$HEROKU_TAR_SHA ] \  
&& tar -xzf heroku-linux-amd64.tar.gz -C /usr/local/lib/ \  
&& ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku \  
&& rm heroku-linux-amd64.tar.gz \  
&& apt-get purge -y wget \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT [ "/usr/local/bin/heroku" ]  

