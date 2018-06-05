FROM ubuntu  
RUN apt-get update && apt-get install -y wget make libreadline-dev gcc  
RUN apt-get install unzip # merge with line above  
RUN wget http://www.lua.org/ftp/lua-5.3.4.tar.gz  
RUN tar zxf lua-5.3.4.tar.gz  
WORKDIR lua-5.3.4  
RUN make linux install  
WORKDIR /  
RUN wget http://luarocks.github.io/luarocks/releases/luarocks-2.4.3.tar.gz  
RUN tar zxf luarocks-2.4.3.tar.gz  
WORKDIR luarocks-2.4.3  
RUN ./configure && make build && make install  
RUN luarocks install busted  
RUN luarocks install lua-mock  
WORKDIR /app  
ENTRYPOINT busted .  

