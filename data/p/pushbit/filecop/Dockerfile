FROM pushbit/ruby  
  
MAINTAINER Tom Moor "tom.moor@gmail.com"  
RUN /bin/bash -l -c "gem install filecop"  
RUN /bin/bash -l -c "gem install faraday"  
  
ADD ./execute.rb ./execute.rb  
  
CMD ["ruby", "./execute.rb"]

