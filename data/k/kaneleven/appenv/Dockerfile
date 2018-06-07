FROM ruby  
  
ENV BUILD_PACKAGES build-essential default-jdk python python-dev python-pip
libpq-dev nodejs  
ENV APP_HOME /app  
  
#RUN sed -i 's/httpredir.debian.org/mirrors.aliyun.com/' /etc/apt/sources.list  
RUN apt-get update -qq && \  
apt-get install -y $BUILD_PACKAGES && \  
mkdir -p $APP_HOME && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR $APP_HOME  
  
ADD . $APP_HOME  
RUN pip install -r requirements.txt && \  
bundle install --without test development

