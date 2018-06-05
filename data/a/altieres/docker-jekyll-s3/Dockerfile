FROM ruby:2.4.1  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
## Python for awscli install & nodejs for assets  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential libpq-dev rsync python-dev nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
# awscli  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install awscli  
  
## Jekyll  
WORKDIR /usr/src/app  
  
RUN gem install jekyll  
  
CMD ["bundle", "exec", "jekyll", "serve", "--force_polling", "--host",
"0.0.0.0"]  
EXPOSE 4000  

