FROM ruby:2.3  
ENV AWS_ACCESS_KEY_ID=changeme  
ENV AWS_SECRET_ACCESS_KEY=changeme  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
COPY Gemfile* ./  
RUN bundle install  
COPY . .  
  
EXPOSE 3000  
CMD ["rails", "server", "-b", "0.0.0.0"]  

