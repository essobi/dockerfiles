#http://qiita.com/hnakamur/items/0b72590136cece29faee  
FROM typista/nginx-nodejs  
#FROM typista/nginx-nodejs:0.7  
RUN wget https://raw.githubusercontent.com/typista/docker-
mean/master/files/entrypoint.sh -O /etc/entrypoint.sh && \  
wget https://raw.githubusercontent.com/typista/docker-
mean/master/files/mongodb.repo -O /etc/yum.repos.d/mongodb.repo && \  
yum update -y && \  
yum -y install mongodb-org && \  
chmod +x /etc/entrypoint.sh  
#EXPOSE 80  
#ENTRYPOINT /etc/entrypoint.sh  

