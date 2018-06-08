FROM ruby:2.5-alpine  
WORKDIR /markup  
  
RUN apk --no-cache add build-base make  
RUN gem install --no-document \  
html-pipeline redcarpet commonmarker gemoji rinku sanitize escape_utils rouge  
RUN apk del build-base  
  
ADD ./files/Makefile .  
ADD ./files/html-pipeline .  
  
ENV LANG en_US.utf8  
  
ENTRYPOINT [""]  
CMD ["make", "all"]  

