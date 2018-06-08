FROM ruby:2.2.3-slim  
RUN apt-get update && \  
apt-get install -y --no-install-recommends build-essential libcurl3
libcurl3-gnutls libcurl4-openssl-dev && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir -p /app  
WORKDIR /app  
COPY Gemfile /app  
RUN bundle install  
COPY . /app  
EXPOSE 5250  
WORKDIR /app  
ENV CATALOGUES_URL http://son-catalogue-repos:4011/catalogues/api/v2  
ENV PORT 5250  
CMD ["foreman", "start"]  

