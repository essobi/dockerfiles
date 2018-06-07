from python:2.7-jessie  
run apt-get update && \  
apt-get -y install sudo unzip ansible  
workdir /cm  
run addgroup --system --gid 981 herbie_bot && \  
adduser --system --uid 981 --gid 981 --home /home/herbie_bot herbie_bot  
RUN echo "herbie_bot ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/herbie_bot && \  
chmod 0440 /etc/sudoers.d/herbie_bot  
user herbie_bot  
workdir /home/herbie_bot  
  

