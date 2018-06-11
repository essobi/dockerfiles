FROM debian  
  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install curl -y  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install nodejs -y  
  
# Tools  
RUN apt-get install vim -y  
RUN apt-get install git -y  
  
CMD /bin/bash  

