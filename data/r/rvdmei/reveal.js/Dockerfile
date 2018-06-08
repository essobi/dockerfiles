FROM node:5.3.0  
RUN npm install -g grunt-cli  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN git clone https://github.com/hakimel/reveal.js.git . && \  
npm install  
  
EXPOSE 8000  
ENTRYPOINT ["grunt"]  
  
CMD ["serve"]  

