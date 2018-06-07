FROM google/python  
  
EXPOSE 8080  
WORKDIR /app  
RUN virtualenv /env  
ADD . /  
  
CMD []  
ENTRYPOINT ["/env/bin/python", "-m", "SimpleHTTPServer", "8080"]  

