FROM ubuntu:latest  
  
#RUN mkdir /home/linuxbrew/  
#RUN mkdir /home/linuxbrew/.linuxbrew  
#RUN mkdir /home/linuxbrew/.linuxbrew/lib/  
#RUN mkdir /home/progtricks  
#RUN mkdir /home/progtricks/codes /home/progtricks/bins  
#COPY deps/ld-linux-x86-64.so.2 /home/linuxbrew/.linuxbrew/lib/ld.so  
#COPY deps/libc.so.6 /home/progtricks/bins  
WORKDIR /home/progtricks  
  
COPY codes codes  
COPY bins bins  
ENTRYPOINT ["/bin/bash"]  

