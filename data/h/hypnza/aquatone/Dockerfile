FROM andrius/alpine-ruby  
  
RUN apk update  
RUN apk add libffi-dev ruby-dev build-base  
  
RUN echo "gem: --no-rdoc --no-ri" >> ~/.gemrc  
RUN gem install aquatone  
  
RUN apk del libffi-dev ruby-dev build-base  
RUN rm -rf /var/cache/apk/*  

