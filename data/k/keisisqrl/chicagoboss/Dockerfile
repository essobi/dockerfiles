FROM erlang:18  
RUN git clone -b v0.9.pre-alpha-2 --depth 1
https://github.com/ChicagoBoss/ChicagoBoss  
  
WORKDIR /ChicagoBoss  
  
RUN make  
  
EXPOSE 8001  
CMD bash  

