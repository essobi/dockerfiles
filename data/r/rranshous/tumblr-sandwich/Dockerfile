FROM ruby:2.2.0  
MAINTAINER "Robby Ranshous <rranshous@gmail.com>"  
WORKDIR /app  
ENV OUTDIR /data  
COPY ./ /app  
RUN bundle install  
RUN mkdir /data  
  
VOLUME /data  
  
ENTRYPOINT ["bundle", "exec", "ruby", "package_blog.rb"]  

