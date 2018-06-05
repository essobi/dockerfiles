FROM ruby:2.5.1  
ENV LANG=C.UTF-8  
COPY Rakefile /usr/local/ruby_code_quality_metrics/Rakefile  
COPY Gemfile /usr/local/ruby_code_quality_metrics/Gemfile  
COPY Gemfile.lock /usr/local/ruby_code_quality_metrics/Gemfile.lock  
  
WORKDIR /usr/local/ruby_code_quality_metrics  
RUN bundle check || bundle install  
COPY . /usr/local/ruby_code_quality_metrics  
  
WORKDIR /app  
  
ENTRYPOINT ["rake", "-f", "/usr/local/ruby_code_quality_metrics/Rakefile"]  

