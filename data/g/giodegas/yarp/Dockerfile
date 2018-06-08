FROM tutum/ubuntu:trusty  
  
MAINTAINER Giovanni De Gasperis <giovanni@giodegas.it>  
  
RUN sh -c 'echo "deb http://www.icub.org/ubuntu trusty contrib/science" >
/etc/apt/sources.list.d/icub.list'  
RUN apt-get update && apt-get upgrade -q -y  
RUN apt-get install -q -y yarp && yarp check  
  
# open port to interact with it  
EXPOSE 10000/tcp  

