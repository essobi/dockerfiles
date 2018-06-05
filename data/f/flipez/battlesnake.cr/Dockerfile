FROM crystallang/crystal  
WORKDIR /app  
ADD . /app  
RUN shards install  
RUN crystal build ./src/battlesnake.cr --release  
RUN chmod +x ./battlesnake  
CMD ./battlesnake  

