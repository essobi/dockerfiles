FROM kisenka/centos6-ruby  
  
RUN yum install -y nodejs npm  
RUN gem install jekyll --no-ri --no-rdoc  
  
VOLUME /data  
  
WORKDIR /data  
EXPOSE 4000  
CMD jekyll serve --host=0.0.0.0 --port=4000 --watch --force_polling  

