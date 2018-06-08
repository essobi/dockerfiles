FROM ubuntu  
  
#ENV megatoolsFile megatools-1.9.94.tar.gz  
RUN apt-get update && apt-get -y install build-essential libglib2.0-dev
libssl-dev libcurl4-openssl-dev libgirepository1.0-dev glib-networking-
services  
  
#COPY megatools-1.9.94 megatools-1.9.94  
COPY megatools-1.9.94.tar.gz megatools-1.9.94.tar.gz  
  
RUN ls  
RUN ["/bin/gzip", "-d", "megatools-1.9.94.tar.gz"]  
RUN ["/bin/tar", "-zxv", "-f", "megatools-1.9.94.tar"]  
  
# change to folder megatools-1.9.94  
WORKDIR /megatools-1.9.94  
RUN ["/bin/bash", "configure"]  
RUN ["/usr/bin/make"]  
  
CMD ["/bin/bash"]

