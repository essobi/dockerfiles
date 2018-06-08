FROM debian:latest  
  
# yum installs  
RUN apt-get -y update && apt-get -y install \  
curl \  
git \  
nodejs \  
npm  
  
# npm installs  
RUN npm install -g \  
nodemon \  
pencilblue-cli  
  
# PencilBlue installation  
RUN mkdir -p /root/pb \  
&& cd /root/pb \  
&& git clone https://github.com/pencilblue/pencilblue.git /root/pb \  
&& npm install  
RUN ln -s `which nodejs` /usr/local/bin/node  
  
ADD config.js /root/pb/temp_config.js  
ADD entrypoint.sh /entrypoint.sh  
  
WORKDIR /root/pb  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["pencilblue", "start"]  
EXPOSE 5002  

