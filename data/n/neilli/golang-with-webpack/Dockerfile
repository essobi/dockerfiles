FROM golang  
RUN apt-get update -y  
RUN apt-get install -y build-essential libssl-dev curl upx  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g webpack webpack-cli  
RUN npm install -g typescript  
RUN go get -u github.com/jessevdk/go-assets-builder  

