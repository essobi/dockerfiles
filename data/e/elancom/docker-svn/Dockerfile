FROM ubuntu:trusty  
  
MAINTAINER lanzx  
  
WORKDIR /  
  
RUN apt-get update \  
&& apt-get install subversion -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /svn  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh", "/bin/bash"]  
  
EXPOSE 3690  

