FROM nginx:latest  
  
# for node to compile native modules  
RUN apt-get update  
RUN apt-get install curl build-essential python git -y  
  
# for node  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  

