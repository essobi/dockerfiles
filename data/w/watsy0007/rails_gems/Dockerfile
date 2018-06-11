FROM watsy0007/rails:5.0.0.1  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install libpq-dev libmysqlclient-dev -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /tmp/bundler  
WORKDIR /tmp/bundler  
COPY Gemfile /tmp/bundler  
RUN bundle install  
  
CMD ['bash']  

