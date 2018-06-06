FROM ruby:2.2-alpine  
LABEL maintainer "Ziyu Wang <odduid@gmail.com>"  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . .  
  
RUN apk --no-cache add g++ make \  
&& bundle install --deployment  
  
EXPOSE 25  
CMD ["ruby", "./mailanalyst.rb"]  

