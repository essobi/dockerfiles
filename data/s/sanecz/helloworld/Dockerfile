FROM ubuntu  
RUN apt-get update && apt-get install -y gcc  
COPY hello.c /home/root/hello/  
WORKDIR /home/root/hello  
RUN gcc hello.c -o hello  
CMD ["pouet", "pouet", "pouet"]  
ENTRYPOINT ["./hello"]  
  

