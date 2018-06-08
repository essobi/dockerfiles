FROM ruby:2.5.1-stretch  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
# Gems are installed without documentation  
# Use `~>` to avoid conflicts  
RUN set -ex; \  
gem install \  
# Core Extensions  
# https://rubygems.org/gems/activesupport/versions/5.2.0  
# (installed with rails 5.2.0)  
# Database Drivers  
# https://rubygems.org/gems/pg/versions/1.0.0  
pg:'~> 1.0.0' \  
# https://rubygems.org/gems/redis/versions/4.0.1  
redis:'~> 4.0.1' \  
# https://rubygems.org/gems/mongo/versions/2.5.3  
mongo:'~> 2.5.3' \  
# https://rubygems.org/gems/sqlite3/versions/1.3.13  
sqlite3:'~> 1.3.13' \  
# Database Tools  
# https://rubygems.org/gems/sequel/versions/5.8.0  
sequel:'~> 5.8.0' \  
# ORM/ODM  
# https://rubygems.org/gems/mongoid/versions/7.0.1  
mongoid:'~> 6.2.0' \  
# HTTP Client  
# https://rubygems.org/gems/faraday/versions/0.15.1  
faraday:'~> 0.15.1' \  
# HTML/XML Parsing  
# https://rubygems.org/gems/nokogiri/versions/1.8.2  
nokogiri:'~> 1.8.2' \  
# Testing: Frameworks  
# https://rubygems.org/gems/rspec/versions/3.7.0  
rspec:'~> 3.7.0' \  
# https://rubygems.org/gems/rspec-its/versions/1.2.0  
rspec-its:'~> 1.2.0' \  
# Testing: Data  
# https://rubygems.org/gems/faker/versions/1.8.7  
faker:'~> 1.8.7' \  
# https://rubygems.org/gems/factory_bot/versions/4.8.2  
# (previously called 'factory_girl')  
factory_bot:'~> 4.8.2' \  
# Web Frameworks  
# https://rubygems.org/gems/rails/versions/5.2.0  
rails:'~> 5.2.0' \  
# https://rubygems.org/gems/sinatra/versions/2.0.1  
sinatra:'~> 2.0.1' \  
# Web Servers  
# https://rubygems.org/gems/rack/versions/2.0.5  
rack:'~> 2.0.5' \  
;  
  
WORKDIR /workspace  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

