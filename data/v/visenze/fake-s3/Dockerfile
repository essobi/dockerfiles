FROM ruby:2.1  
# install fake-s3  
RUN gem install fakes3  
  
# run fake-s3  
RUN mkdir -p /fakes3_root  
ENTRYPOINT ["fakes3"]  
CMD ["-r", "/fakes3_root", "-p", "80"]  
EXPOSE 80  

