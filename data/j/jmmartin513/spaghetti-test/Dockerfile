FROM ubuntu AS compiler  
RUN apt-get update  
RUN apt-get install -y build-essential  
COPY hello.c /  
RUN make hello  
FROM ubuntu  
COPY \--from=compiler /hello /hello  
CMD /hello  

