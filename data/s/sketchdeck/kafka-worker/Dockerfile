FROM sketchdeck/base-coffee  
  
COPY . /src  
WORKDIR /src  
  
RUN rm -rf node_modules  
RUN npm cache clean  
RUN npm install  
  
#I know the keys are still in the container images but this makes it less
likely that they will be revealved by a security issue in the running
application  
RUN rm -rf /root/.ssh  
  
CMD ["coffee", "app.coffee"]  

