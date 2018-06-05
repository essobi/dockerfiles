FROM node:7.7-onbuild  
LABEL maintainer="John Berlin:jberlin@cs.odu.edu" \  
WSDL="Web Science and Digital Libraries Research Group, ODU CS" \  
descriptoin="Fixes the issues that caused the homepage of \  
http://cnn.com from being replayed from Internet Archives Wayback Machine \  
http://ws-dl.blogspot.com/2017/01/2017-01-20-cnncom-has-been-
unarchivable.html" \  
version="1.0.0"  
  
RUN apt-get update  
  
ENV NODE_ENV production  
  
EXPOSE 3000  
CMD ["sh", "run.sh"]

