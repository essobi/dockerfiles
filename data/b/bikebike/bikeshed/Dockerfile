############  
# BikeShed #  
############  
# login for test users on website  
FROM bikebike/bikebike  
MAINTAINER Jonathan Rosenbaum <gnuser@gmail.com>  
  
RUN git clone git://github.com/spacemunkay/BikeShed.git  
RUN gem install bundler  
RUN apt-get update && apt-get -y install libpq-dev postgresql-9.3 g++ unzip  
RUN bundle install --gemfile=/BikeShed/Gemfile; \  
cd /BikeShed; gem install rake -v '10.1.1'; \  
gem install therubyracer -v '0.10.2'  
COPY pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf  
  
# Because of an undefined constant SeedBike  
COPY seeds.rb /BikeShed/db/seeds.rb  
RUN cp /BikeShed/config/database.yml.example /BikeShed/config/database.yml; \  
service postgresql start; \  
cd /BikeShed; \  
sudo -u postgres -i createuser -d -w velocipede; \  
adduser --disabled-password --gecos "" velocipede; \  
sudo -u velocipede -i createdb -U velocipede --owner=velocipede velocipede; \  
sudo -u velocipede -i createdb -U velocipede --owner=velocipede
velocipede_test; \  
  
bundle exec rake db:create db:migrate; \  
bundle exec rake db:seed  
  
  
COPY postgresql.conf bikeshed.conf /etc/supervisor/conf.d/  
#COPY bikeshed.conf /etc/supervisor/conf.d/  
COPY extjs-4.1.1.zip /BikeShed/  
  
RUN cd /BikeShed; \  
unzip extjs-4.1.1.zip; \  
ln -s /BikeShed/ext-4.1.1a /BikeShed/public/extjs  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
  
# docker run -d -p 3000:3000 --name="freehub" bikebike/freehub  

