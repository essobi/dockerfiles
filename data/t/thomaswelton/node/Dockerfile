FROM thomaswelton/ubuntu  
  
MAINTAINER thomaswelton  
  
# GET NODE INSTALL DEPS  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential python
wget  
  
# NODE V0.10.26  
RUN wget http://nodejs.org/dist/v0.10.26/node-v0.10.26.tar.gz  
RUN tar -zxvf node-v0.10.26.tar.gz  
RUN rm node-v0.10.26.tar.gz  
WORKDIR node-v0.10.26  
  
# INSTALL NODE  
RUN ./configure  
RUN make  
RUN make install  
  
# CLEAN UP  
WORKDIR ..  
RUN rm -r node-v0.10.26  
RUN apt-get remove -y build-essential python wget  

