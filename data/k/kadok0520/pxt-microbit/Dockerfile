FROM node:alpine  
MAINTAINER Hong-Da, Ke  
  
RUN mkdir -p /root/pxt-microbit \  
&& cd /root/pxt-microbit \  
&& npm install -g pxt \  
&& pxt target microbit  
  
EXPOSE 80 3233  
WORKDIR /root/pxt-microbit  
  
ENTRYPOINT ["pxt", "serve", "-h", "0.0.0.0", "-p", "80","--noBrowser"]  

