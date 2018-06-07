FROM ruby:2.1.4  
MAINTAINER johnjansen  
EXPOSE 3000  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
RUN git clone https://github.com/seomoz/qless.git  
WORKDIR /usr/src/app/qless  
COPY ./config.ru /usr/src/app/qless/config.ru  
RUN bundle install  
CMD ["thin", "start"]  

