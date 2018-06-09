FROM steinwaywhw/pandoc  
RUN apt-get update && \  
apt-get install -y nano python-pygments autoconf bison build-essential libssl-
dev libyaml-dev libreadline6-dev \  
zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev nodejs npm && \  
apt-get clean  
  
RUN apt-get install -y ruby2.3 ruby2.3-dev  
RUN gem install bundler jekyll  
  
EXPOSE 4000  

