FROM node:0.10  
  
MAINTAINER Tomohisa Kusano <siomiz@gmail.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
sudo  
  
RUN npm install tty.js -g \  
&& npm cache clean  
  
RUN useradd -d /home/user user \  
&& mkdir -p /home/user/.tty.js \  
&& chown -R user.user /home/user \  
&& adduser user sudo \  
&& echo "user ALL=NOPASSWD: ALL" > /etc/sudoers.d/user  
  
ADD cmd.js /cmd.js  
  
USER user  
  
WORKDIR /home/user  
  
CMD ["/usr/local/bin/node", "/cmd.js"]  
  
EXPOSE 8080  

