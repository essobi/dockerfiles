FROM node:argon  
  
RUN mkdir -p /usr/src  
RUN mkdir -p /etc/app  
COPY conf.yaml /etc/app/conf.yaml  
RUN git clone \--branch 0.0.1 https://github.com/clebi/auth-server.git
/usr/src/app  
WORKDIR /usr/src/app  
RUN npm install  
  
CMD ["./node_modules/.bin/sequelize", "db:migrate", "--conf",
"/etc/app/conf.yaml"]  

