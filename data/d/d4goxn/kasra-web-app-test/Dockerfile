FROM node:5  
  
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y curl git
ruby tar wget build-essential  
  
RUN gem install sass  
  
COPY . /opt/kasra-web-app/  
  
WORKDIR /opt/kasra-web-app  
  
RUN npm --no-color install  
RUN npm --no-color run build  
  
RUN gem uninstall -x sass  
  
EXPOSE 3000  
CMD ["npm", "start"]  

