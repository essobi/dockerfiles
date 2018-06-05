FROM ruby  
MAINTAINER Ryan Ratcliff <ryan.ratcliff@ryanratcliff.net>  
  
EXPOSE 4568  
  
RUN mkdir -p /var/lib/sqs  
  
WORKDIR /var/lib/sqs  
RUN cd /var/lib/sqs  
RUN git clone https://github.com/RyanRatcliff/yafake_sqs.git  
RUN cd yafake_sqs  
WORKDIR /var/lib/sqs/yafake_sqs  
RUN gem build yafake_sqs.gemspec  
RUN gem install yafake_sqs  
CMD ["yafake_sqs", "--database" , "/var/lib/sqs/yafake_sqs/database.yml"]  

