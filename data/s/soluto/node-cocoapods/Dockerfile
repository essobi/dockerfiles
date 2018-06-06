FROM node:6  
  
# Add ruby and cocoapods  
RUN apt-get update  
RUN apt-get install -y ruby-full  
RUN apt-get install -y unzip  
# Packaged `activesupport` incompatible  
# with packaged `ruby` version  
RUN gem install activesupport -v 4.2.6  
  
RUN gem install cocoapods  
  
# You cannot run CocoaPods as root  
# (user `nobody` does not have enough permissions)  
USER node  
  
ENV LANG C.UTF-8  
  
RUN pod setup  

