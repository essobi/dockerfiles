FROM jagregory/lua  
MAINTAINER James Gregory <james@jagregory.com>  
  
# install busted from luarocks  
RUN luarocks install busted  
  
# create the source directory  
RUN mkdir /source  
WORKDIR /source  
  
ENTRYPOINT ["busted"]  
CMD ["specs"]  

