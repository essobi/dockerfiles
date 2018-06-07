FROM ruby:2.4.2-alpine3.6  
ENV PK_RUBY build-base libstdc++  
  
RUN apk --update --no-cache add $PK_RUBY  
WORKDIR /app  
  
RUN gem install marc  
  
ADD ./scripts/ybp.rb /app/ybp  
ADD ./scripts/casalini.rb /app/casalini  
ADD ./scripts/harrassowitz.rb /app/harrassowitz  
ADD ./scripts/amalivre.rb /app/amalivre  
RUN chmod +x /app/*  
ENV PATH /app:$PATH  

