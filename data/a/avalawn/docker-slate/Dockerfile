# For local development of slate documentation.  
#  
# Usage:  
# > docker run -rm -i -t -v $PWD:/app -p 4567:4567 ctclearhaus/slate  
# Browse http://localhost:4567  
FROM debian  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install --yes curl git procps  
RUN curl -sSL https://get.rvm.io | bash -s stable && gpasswd -a root rvm  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.0.0-p353"  
RUN apt-get install --yes rubygems  
RUN /bin/bash -l -c "gem update --system && gem install bundler --no-ri --no-
rdoc"  
  
ENV DEBIAN_FRONTEND dialog  
  
WORKDIR /app  
RUN git clone https://github.com/tripit/slate.git  
  
WORKDIR /app/slate  
RUN /bin/bash -l -c "bundle install"  
  
#WORKDIR /app  
CMD /bin/bash -l -c "bundle exec middleman server"  
EXPOSE 4567  

