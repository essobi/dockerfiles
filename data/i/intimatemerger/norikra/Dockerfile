FROM jruby:9.1.8-alpine  
  
LABEL maintainer "mats116 <mats.kazuki@gmail.com>"  
  
RUN gem install norikra:1.4.0 --no-ri --no-rdoc  
  
EXPOSE 26571 26578  
CMD norikra start  

