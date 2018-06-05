FROM amazonlinux  
  
RUN curl -sL https://rpm.nodesource.com/setup_6.x | bash - \  
&& yum -y update \  
&& yum -y install nodejs findutils gcc-c++ make git openssh-client aws-cli
which  
  
RUN npm install npm@5.8.0  
RUN rm -rf /usr/lib/node_modules/npm  
RUN mv node_modules/npm /usr/lib/node_modules/npm  
  
EXPOSE 3000  
  
CMD [ "node" ]

