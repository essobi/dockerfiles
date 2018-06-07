FROM ruby:slim  
  
RUN \  
apt-get update && apt-get install -y --no-install-recommends \  
git \  
openssh-client \  
postgresql-client \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
curl https://toolbelt.heroku.com/install.sh | sh && \  
/usr/local/heroku/bin/heroku --version  
  
ENV PATH $PATH:/usr/local/heroku/bin  
  
ENTRYPOINT ["heroku"]  

