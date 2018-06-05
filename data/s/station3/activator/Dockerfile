FROM station3/activator:1.3-minimal  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY . /usr/src/app/  
  
CMD [ "activator", "run" ]

