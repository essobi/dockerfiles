FROM node:0.12  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN npm install -g ttyrec ttycast  
  
WORKDIR /work  
ENV TERMSIZE 200x40  
  
CMD mkfifo -m 666 /work/ttycast && ttyplay -n /work/ttycast | ttycast -s
${TERMSIZE}; rm /work/ttycast  
  

