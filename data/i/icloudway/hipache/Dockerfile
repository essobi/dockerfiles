# This file describes how to build Hipache into a runnable linux container
with  
# all dependencies installed.  
#  
# To build:  
#  
# 1) Install docker (http://docker.io)  
# 2) Clone Hipache repo if you haven't already: git clone
https://github.com/dotcloud/hipache.git  
# 3) Build: cd hipache && docker build .  
# 4) Run: docker run -d --name redis redis  
# 5) Run: docker run -d --link redis:redis -P <hipache_image_id>  
#  
# See the documentation for more details about how to operate Hipache.  
from debian:jessie  
  
# Update & Install node and npm  
run apt-get update && \  
apt-get install -y --no-install-recommends nodejs npm supervisor redis-server
&& \  
rm -rf /var/lib/apt/lists/*  
  
# Manually add Hipache folder  
copy . ./hipache  
  
# Then install it  
run npm install -g ./hipache --production  
  
# This is provisional, as we don't honor it yet in Hipache  
env NODE_ENV production  
  
# Create Hipache log directory  
run mkdir -p /var/log/hipache  
  
# Make change to redis configuration  
run sed -i 's/daemonize yes/daemonize no/' /etc/redis/redis.conf  
  
# Add supervisor conf  
copy ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Expose Hipache  
expose 80  
# Start Hipache  
cmd ["supervisord", "-n"]  

