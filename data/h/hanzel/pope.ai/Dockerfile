FROM quay.io/hanzeljesheen/nodejs  
  
WORKDIR /src  
ADD . /src  
  
RUN apk update && apk upgrade && apk --update add ruby ruby-irb ruby-rdoc &&
rm -rf /var/cache/apk/*  
RUN gem install sass  
  
RUN npm install -g nodemon  
RUN npm install -g gulp  
RUN npm install  
RUN gulp build  
  
EXPOSE 8000  
CMD ["npm", "start"]

