FROM tangpei506/nodejs:frontbase  
  
# process user files  
ADD etc /etc/  
WORKDIR /usr/src/app/  
RUN bower install && \  
gem install sass compass  
RUN grunt build  
RUN mkdir /usr/html && cp -rf dist/* /usr/html && rm -rf *  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

