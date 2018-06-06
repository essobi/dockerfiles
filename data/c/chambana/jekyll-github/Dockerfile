FROM chambana/base:latest  
  
MAINTAINER Josh King <jking@chambana.net>  
  
ENV JEKYLL_GITHUB_BRANCH="master" \  
JEKYLL_GITHUB_SUBDIR="/"  
RUN apt-get -qq update && \  
apt-get install -y --no-install-recommends ruby ruby-dev git build-essential
patch zlib1g-dev liblzma-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install jekyll bundler  
  
EXPOSE 4000  
ADD bin/run.sh /app/bin/run.sh  
RUN chmod +x /app/bin/run.sh  
  
ENTRYPOINT ["/app/bin/run.sh"]  
CMD ["jekyll", "serve", "-H", "0.0.0.0"]  

