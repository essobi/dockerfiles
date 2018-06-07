FROM java:8  
# Do a general update to help downstream container bulids  
RUN apt-get clean && apt-get update  
  
# install node  
RUN wget -qO- https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# install awscli  
RUN apt-get install -y awscli  
  
# install serverless  
RUN npm install -g serverless  
  
# Add a default Command  
CMD ["bash"]  

