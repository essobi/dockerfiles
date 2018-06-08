FROM debian:jessie  
  
RUN apt-get update && apt-get install -y packaging-dev checkinstall libboost-
graph-dev libpq-dev libexpat1-dev postgresql-client libboost-program-options-
dev && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ADD . /app  
WORKDIR /app  
  
RUN cmake -H. -Bbuild  
WORKDIR /app/build  
RUN make  
RUN make install  

