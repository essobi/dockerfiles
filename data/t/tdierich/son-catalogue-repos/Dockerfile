FROM ruby:2.2.3-slim  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential && \  
apt-get -y install libcurl3 libcurl3-gnutls libcurl4-openssl-dev && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir -p /app  
COPY Gemfile /app/  
WORKDIR /app  
RUN bundle install  
COPY . /app  
RUN rake yard  
ENV PORT 4002  
#ENV MAIN_DB son-catalogue-repository  
#ENV MAIN_DB_HOST mongo:27017  
#ENV SECOND_DB son-catalogue-repository  
#ENV SECOND_DB_HOST mongo:27017  
EXPOSE 4002  
WORKDIR /app  
CMD ["rake", "start"]  

