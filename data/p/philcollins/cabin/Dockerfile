FROM philcollins/aurora-centos7  
  
RUN curl -sL https://rpm.nodesource.com/setup_4.x | bash -  
RUN yum install -y nodejs  
RUN yum install -y http://dev.mysql.com/get/mysql-community-release-
el7-5.noarch.rpm  
RUN yum install -y mysql-community-client  
RUN yum install -y git  
RUN git clone https://github.com/ssalevan/stream-react-example.git  
WORKDIR /stream-react-example/app  
RUN npm install  
WORKDIR /stream-react-example/api  
RUN npm install  
WORKDIR /stream-react-example  
RUN npm install -g webpack nodemon  
ADD env.sh .  
ADD start.sh .  
RUN chmod +x start.sh  
CMD ./start.sh  
EXPOSE 3000  
EXPOSE 8000  
RUN yum erase -y git  
  

