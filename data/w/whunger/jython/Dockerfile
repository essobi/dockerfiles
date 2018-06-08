FROM whunger/jython:2.5.3  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip --insecure install -r requirements.txt  
  
ONBUILD COPY . /usr/src/app  

