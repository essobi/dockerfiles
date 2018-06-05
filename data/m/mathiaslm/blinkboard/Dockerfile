FROM node:wheezy  
  
# Clone project  
RUN git clone https://github.com/mathiaslm89/BlinkBoard.git /usr/BlinkBoard/  
  
# Set working directory  
WORKDIR /usr/BlinkBoard  
  
# Install dependencies  
RUN npm install  
  
# Hack to allow bower to install dependencies inside docker (requires root
permissions)  
RUN chown -R root /usr/BlinkBoard  
RUN npm install -g bower  
RUN bower --allow-root install  
  
# Prepare app  
CMD [ "npm", "start" ]  
  
# How to run  
RUN echo 'run e.g. [docker run -d --env-file=.env -p {port}:{port}
{containerID}]'  

