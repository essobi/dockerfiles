FROM ruby:2-wheezy  
  
MAINTAINER Raphael Michel  
USER root  
  
RUN apt-get update && apt-get install -y build-essential locales curl \  
\--no-install-recommends  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install --yes nodejs  
  
WORKDIR /  
  
RUN locale-gen  
RUN update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN gem install jekyll  
  
CMD ["/bin/bash"]  

