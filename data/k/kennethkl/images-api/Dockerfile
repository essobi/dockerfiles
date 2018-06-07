FROM dockerfile/nodejs  
  
RUN rm -fr /app && mkdir /app  
ADD . /app  
RUN cd /app && npm install  
  
EXPOSE 8000  
CMD cd /app && npm start

