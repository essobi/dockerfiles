FROM nginx:latest  
  
LABEL maintainer "Feng Zhou <feng.zh@gmail.com>"  
  
RUN apt-get update --quiet > /dev/null && \  
apt-get install --assume-yes --force-yes -qq \  
openssh-client sshfs curlftpfs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD autoindex.conf /etc/nginx/conf.d/  
ADD init.sh /  
  
CMD ["/init.sh"]  
  

