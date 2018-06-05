FROM golang  
  
RUN apt-get update && apt-get install -y sqlite3 less  
  
WORKDIR /go/src/Assignment-3  
COPY . .  
  
RUN go-wrapper download  
RUN go-wrapper install  
  
RUN sqlite3 inventory.db<initialDBTables/inventory.txt && \  
sqlite3 users.db<initialDBTables/users.txt && \  
sqlite3 purchase.db<initialDBTables/purchase.txt  
  
CMD ["go-wrapper", "run"]  

