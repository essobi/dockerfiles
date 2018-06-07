FROM ontouchstart/fsharp  
COPY . samples-browser  
RUN cd samples-browser && yarn install && dotnet restore  
RUN cd samples-browser/src && dotnet restore  
  

