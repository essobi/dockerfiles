FROM makevoid/ruby  
  
RUN apt-get update  
RUN apt-get install -y git nodejs npm && \  
npm install coffee-script  
  
# The downside:  
#  
# /usr/bin/nodejs /usr/local/lib/node_modules/coffee-script/bin/coffee  
#  
# TODO: fix this  
CMD ["irb"]  

