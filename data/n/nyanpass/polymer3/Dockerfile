FROM netczuk/node-yarn  
  
MAINTAINER Tomofumi Inoue <funaox@gmail.com>  
  
WORKDIR /root  
  
RUN npm install -g polymer-cli  
  
ADD . ./  
  
RUN yarn install  
  
EXPOSE 8081  
CMD ["polymer", "serve", "--npm", "--hostname", "0.0.0.0", "--port", "8081"]  

