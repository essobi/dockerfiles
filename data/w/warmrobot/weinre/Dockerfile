FROM node:latest  
MAINTAINER Igor Frolov imfrolov@gmail.com  
RUN npm i -g weinre  
EXPOSE 8080  
ENTRYPOINT ["/usr/local/bin/weinre", "--httpPort", "8080", "--boundHost",
"-all-"]  

