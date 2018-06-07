FROM ruby:2.4.3  
  
ENV LC_ALL=C.UTF-8  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && \  
apt-get install -y \  
mysql-client \  
postgresql-client \  
sqlite3 \  
nodejs \  
imagemagick \  
mecab libmecab-dev mecab-ipadic-utf8 \  
unzip \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
RUN npm install -g yarn phantomjs  

