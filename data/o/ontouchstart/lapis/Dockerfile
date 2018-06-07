FROM ontouchstart/openresty  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN luarocks install lapis  
RUN luarocks list  
RUN ln -s /usr/local/openresty/luajit/bin/lapis /usr/local/bin  
RUN rm -rf work  
ADD work work  
RUN cd work && \  
lapis new --lua  
WORKDIR work  
CMD ["./server"]  

