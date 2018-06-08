FROM ubuntu:trusty  
  
RUN apt-get update \  
&& apt-get install -y git  
RUN git clone https://github.com/facebook/fbctf \  
&& cd fbctf \  
&& source ./extra/lib.sh \  
&& quick_setup install prod  
  
CMD ["/bin/bash"]  

