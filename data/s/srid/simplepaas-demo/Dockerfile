FROM ubuntu  
RUN mkdir /data && echo 'hello world' > /data/hello.txt  
WORKDIR /data  
ENV VIRTUAL_HOST test.srid.name  
EXPOSE 80  
CMD ["python3", "-u", "-m", "http.server", "80"]  

