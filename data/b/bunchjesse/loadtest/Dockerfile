FROM node:7.0  
MAINTAINER Jesse Bunch <jesse@getbunch.com>  
  
# Fixes issues with docker exec  
# See https://github.com/dockerfile/mariadb/issues/3  
RUN echo "export TERM=xterm" >> ~/.bashrc  
  
# Install artillery  
RUN npm install -g loadtest  
  
# ENV  
ENV DURATION=20  
ENV NUM_USERS=10  
ENV REQUESTS_PER_SECOND=500  
ENV URL=localhost  
  
CMD loadtest -t $DURATION -c $NUM_USERS \--rps $REQUESTS_PER_SECOND
\--insecure --keepalive $URL

