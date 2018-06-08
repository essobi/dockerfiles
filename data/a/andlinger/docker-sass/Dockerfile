FROM node:9.4.0-stretch  
  
RUN apt-get update \  
&& apt-get install -y rubygems rubygems-integration ruby-all-dev build-
essential python-pip jq jpegoptim optipng \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install sass -v 3.5.3  
RUN pip install yq  
RUN npm install -g svgo  

