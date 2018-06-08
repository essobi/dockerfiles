FROM ruby:2.4.1  
ENV MASTERMIND_VERSION=0.1.0  
ENV MASTERMIND_API_HOST=localhost  
ENV MASTERMIND_API_PORT=3000  
ENV MASTERMIND_UI_HOST=web  
ENV MASTERMIND_UI_PORT=8080  
ENV SERVICE_MANAGER_HOST=service-manager  
ENV SERVICE_MANAGER_PORT=8080  
ENV MASTERMIND_OAUTH_URI=account.lab.fiware.org  
ENV MASTERMIND_OAUTH_CLIENT_ID=f856da058c20414db0e946d234a5b9b1  
ENV MASTERMIND_OAUTH_SECRET_ID=08eaae80ae544d66ba858de71adb7421  
ENV OAUTH_ENABLED=false  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
git  
RUN mkdir /mastermind  
WORKDIR /mastermind  
ADD Gemfile /mastermind/Gemfile  
ADD Gemfile.lock /mastermind/Gemfile.lock  
RUN bundle install  
ADD . /mastermind  
RUN git clone https://github.com/martel-innovate/MasterMind-Service-Catalog
mastermind-services  
  
ENTRYPOINT rails db:setup && rails s -b0  

