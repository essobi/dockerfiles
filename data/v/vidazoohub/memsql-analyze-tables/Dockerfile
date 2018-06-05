#it's small and offical so i'm using it  
FROM alpine:3.5  
#install needed mysql tools  
RUN apk --no-cache add py-mysqldb python  
  
#copy the codebase  
RUN mkdir /memsql-analyze-tables  
COPY ./ /memsql-analyze-tables  
  
#unbuffer for logging sakes  
ENV PYTHONUNBUFFERED=true  
  
#and run it  
CMD python /memsql-analyze-tables/memsql_analyze_tables.py  

