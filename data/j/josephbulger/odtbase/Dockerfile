FROM josephbulger/dotnetnode:1.1.0-sdk-projectjson-6.5.0-node  
  
RUN apt-get update && apt-get install -y --no-install-recommends xsltproc  
  
COPY . /build  
  
WORKDIR /build  
  
RUN dotnet restore  
  
RUN npm install -g local-npm  
  
RUN local-npm  
  
RUN npm set registry http://127.0.0.1:5080  
  
RUN npm install  
  

