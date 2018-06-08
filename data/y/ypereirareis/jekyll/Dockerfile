FROM ypereirareis/docker-node-modules:2.0  
MAINTAINER Yannick Pereira-Reis <yannick.pereira.reis@gmail.com>  
  
# Install common libs  
RUN apt-get update && apt-get install -y \  
openssl \  
libssl-dev \  
make \  
gcc \  
rubygems \  
sudo  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB &&\  
echo progress-bar >> ~/.curlrc &&\  
\curl -sSL https://get.rvm.io | bash -s stable &&\  
bash -l -c 'source /etc/profile.d/rvm.sh && rvm install 2.5.0 && ruby
--version'  
  
# Install bundle  
RUN bash -l -c 'gem install bundler'  
  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
  
# Install all deps  
RUN bash -l -c 'bundle install && bundle update'  
  
VOLUME ["/app"]  
WORKDIR /app  
EXPOSE 4000  
CMD ["bundle", "exec", "jekyll", "serve", "-H0.0.0.0"]  
  

