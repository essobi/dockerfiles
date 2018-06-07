FROM node:alpine  
  
RUN npm install -g write-good \  
&& echo "I stole the cat." > test.md \  
&& write-good *.md \  
&& rm test.md  
  
WORKDIR /app  
VOLUME /app  
  
ENTRYPOINT ["write-good"]  
CMD []  

