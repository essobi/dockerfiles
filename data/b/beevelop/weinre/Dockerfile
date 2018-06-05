FROM beevelop/nodejs:alpine  
  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
RUN npm i -g --unsafe-perm weinre  
  
EXPOSE 8080  
ENTRYPOINT ["weinre"]  
  
CMD ["--httpPort", "8080", "--boundHost", "0.0.0.0", "--debug", "--readTimeout
7"]  

