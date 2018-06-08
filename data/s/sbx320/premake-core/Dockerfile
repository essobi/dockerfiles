FROM sbx320/clang:svn  
  
WORKDIR /src  
  
COPY . /src  
  
RUN make -f Bootstrap.mak linux  
RUN ./bin/release/premake5 embed  
RUN cp ./bin/release/premake5 /bin  
RUN rm -rf /src  

