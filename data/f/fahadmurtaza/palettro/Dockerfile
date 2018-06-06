FROM python:onbuild  
# Create app directory  
RUN mkdir -p /usr/src/app  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
# Install Yarn  
RUN npm install -y -g yarn  
  
# Install node packages  
RUN yarn install  
  
# Move to packages to static folder  
RUN mv node_modules static  
  
EXPOSE 8000  
CMD ["python", "app.py", "-p 8000"]  

