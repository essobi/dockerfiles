#http://qiita.com/hnakamur/items/0b72590136cece29faee  
FROM typista/nginx-lua  
#FROM typista/nginx-lua:0.7  
  
RUN wget https://raw.githubusercontent.com/typista/docker-nginx-
nodejs/master/files/entrypoint.sh -O /etc/entrypoint.sh && \  
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
yum install -y nodejs npm --enablerepo=epel && \  
git clone git://github.com/creationix/nvm.git ~/.node && \  
source ~/.node/nvm.sh && \  
npm install -g grunt-cli && \  
npm install -g forever && \  
npm install -g express && \  
chmod +x /etc/entrypoint.sh  

