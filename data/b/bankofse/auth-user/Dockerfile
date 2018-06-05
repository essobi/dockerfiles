FROM iojs  
  
WORKDIR /src  
  
RUN wget
https://github.com/hashicorp/envconsul/releases/download/v0.5.0/envconsul_0.5.0_linux_amd64.tar.gz  
RUN tar xzf envconsul_0.5.0_linux_amd64.tar.gz  
RUN mv envconsul_0.5.0_linux_amd64/envconsul /usr/bin/  
  
COPY ./ /src  
  
RUN npm install  
  
CMD ./start.sh  

