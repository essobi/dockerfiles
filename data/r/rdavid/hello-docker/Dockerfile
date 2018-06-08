FROM mono:latest  
ADD . /src  
RUN mcs /src/hello.cs  
CMD [ "mono", "/src/hello.exe" ]  

