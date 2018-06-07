FROM node:5.11  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && chmod +x get-pip.py &&
./get-pip.py  
RUN pip install awscli  
  
#Install node json export code  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app  
RUN npm install  
COPY . /usr/src/app  
  
CMD ["bash", "-c", "./backup.sh"]  
  

