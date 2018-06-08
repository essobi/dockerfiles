FROM golang  
  
RUN mkdir /present && \  
go get golang.org/x/tools/cmd/present && \  
go install golang.org/x/tools/cmd/present  
ADD . /present  
  
WORKDIR /present  
EXPOSE 3999  
CMD ["present", "-http", "0.0.0.0:3999"]  

