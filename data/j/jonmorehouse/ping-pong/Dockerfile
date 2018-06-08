FROM jonmorehouse/node  
MAINTAINER Jon Morehouse <morehousej09@gmail.com>  
  
# add in our simple application  
ADD . /app  
RUN cd /app && npm install  
  
# set up default run commands  
EXPOSE 8080  
WORKDIR /app  
ENTRYPOINT ["./node_modules/coffee-script/bin/coffee"]  
CMD ["app.coffee"]  
  

