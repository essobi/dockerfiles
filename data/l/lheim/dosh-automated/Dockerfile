FROM lheim/rails_uhd:latest  
MAINTAINER lennart.heim@rwth-aachen.de  
  
  
RUN cd / && git clone https://github.com/lheim/dosh  
  
WORKDIR /dosh  
  
ENV RAILS_ENV development  
  
RUN bundle install  
  
RUN rake assets:precompile  
  
RUN rake db:migrate  
RUN rake db:seed  
  
EXPOSE 3000  
CMD rails s -b 0.0.0.0  

