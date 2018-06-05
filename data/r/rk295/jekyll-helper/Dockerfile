FROM ubuntu  
  
COPY Gemfile /  
  
RUN apt update && \  
apt-get install -y ruby ruby-dev build-essential curl rsync ssh zlib1g-dev
aspell  
  
RUN gem install jekyll bundler  
  
RUN cd / && bundle install  

