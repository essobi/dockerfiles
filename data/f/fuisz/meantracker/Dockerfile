FROM jongleberry/opencv  
  
ADD . /tracker/  
WORKDIR /tracker/  
  
RUN npm install  
RUN npm dedupe  
RUN npm run postinstall  
  
CMD ["bash"]  

