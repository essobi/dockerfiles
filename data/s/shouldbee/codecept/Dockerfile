FROM ubuntu:14.04  
RUN apt-get update -qq && apt-get install -y php5 php5-mysql php5-curl  
  
ADD http://codeception.com/codecept.phar /usr/local/bin/codecept  
RUN chmod +x /usr/local/bin/codecept  
  
# A simple testing  
RUN php -v | grep "PHP 5.5" && \  
codecept -V --no-ansi | grep "version 2"  
  
ENTRYPOINT ["codecept"]  
CMD ["--help"]  

