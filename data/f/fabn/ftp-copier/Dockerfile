FROM ruby:2.3  
RUN mkdir /opt/ftp  
RUN mkdir /opt/ftp/tmp  
WORKDIR /opt/ftp  
  
ADD ftp-copy.rb /opt/ftp/  
  
CMD ["./ftp-copy.rb"]

