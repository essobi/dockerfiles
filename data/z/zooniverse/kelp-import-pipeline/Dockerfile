FROM zooniverse/ruby:2.3  
RUN apt-get update && \  
apt-get install -y \  
python \  
python-gdal \  
python-skimage \  
libpq-dev \  
libpq5 \  
libmagickwand-dev \  
imagemagick && \  
rm -rf /var/lib/apt/lists/  
  
WORKDIR /src/  
  
COPY Gemfile /src/  
  
RUN bundle install  
  
COPY . /src/  

