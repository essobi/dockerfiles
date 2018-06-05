FROM seldszar/liquidsoap:1.2.1  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY . /usr/src/app/  
  
CMD ["liquidsoap", "ls_script.liq"]  

