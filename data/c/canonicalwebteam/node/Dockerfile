FROM node:7-slim  
  
# Install bower  
RUN apt-get update && apt-get install --yes git python build-essential  
RUN update-alternatives --set cc /usr/bin/gcc  
RUN npm install -u -g bower yarn node-sass  
  
# Create a shared home directory - this helps anonymous users have a home  
ENV HOME=/home/shared LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN mkdir -p $HOME  
RUN mkdir -p $HOME/.cache/yarn/  
RUN mkdir -p $HOME/.cache/bower/  
RUN chmod -R 777 $HOME  
  
# Use bash as the default interpreter  
ENTRYPOINT []  
CMD ["/bin/bash"]  
  

