FROM ruby:latest  
  
# Install random stuff  
RUN apt-get update && \  
apt-get install -y --no-install-recommends rsync && \  
rm -rf /var/lib/apt/lists/*  
# Install gems  
RUN gem install bundler  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y --no-install-recommends nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g yarn  
  
WORKDIR /source  

