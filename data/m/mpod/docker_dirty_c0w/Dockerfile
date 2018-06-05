FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y gcc cpp curl cowsay ruby  
RUN curl
https://raw.githubusercontent.com/dirtycow/dirtycow.github.io/master/dirtyc0w.c
> dirtyc0w.c  
RUN gcc -static -s -pthread dirtyc0w.c -o dirtyc0w  
ADD post_status.rb .  
RUN gem install librato-metrics  
ADD testing-dirtycow.sh .  
CMD ./testing-dirtycow.sh  

