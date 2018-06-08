FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq -y && apt-get install -qq -y nodejs npm git git-core
g++  
RUN apt-get clean  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install forever -g  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
CMD /run.sh  

