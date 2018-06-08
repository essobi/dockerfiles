FROM jongleberry/opencv  
  
ADD . /tracker/  
WORKDIR /tracker/  
  
RUN npm install  
RUN npm dedupe  
# getting ldconfig-related errors if i don't rebuild...  
RUN npm rebuild  
  
EXPOSE 3022  
CMD ["./bin/server"]  

