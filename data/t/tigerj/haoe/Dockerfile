# fixed base image  
FROM ubuntu  
  
# apt-get installs for ubuntu  
RUN apt-get update && apt-get -y install \  
git \  
gcc \  
nano \  
vim  
  
# make workdir  
RUN mkdir -p /home/haoe/booksrc/bin  
  
# get 'Hacking: The Art of Exploitation' source  
COPY /booksrc /home/haoe/booksrc  
  
# set workdir  
WORKDIR /home/haoe  

