FROM paul91/puppetbase  
MAINTAINER Paul Lewis <paullewis91@gmail.com>  
  
RUN yum install -y git tar  
ADD Puppetfile /  
RUN librarian-puppet install  
RUN puppet apply --modulepath=/modules -e "class { 'epel':}->class { 'nodejs':
}"  
  
ADD . /src  
RUN npm install -g inherits n; n 0.11.12  
RUN cd /src; npm install  
  
EXPOSE 3000  
CMD ["node", "--harmony", "/src/app.js"]  

