FROM ubuntu:15.10  
WORKDIR /root  
RUN apt-get update -y  
RUN apt-get install -y nginx-extras luajit lua-cjson  
RUN apt-get install -y curl tree default-jre libimage-exiftool-perl  
  
# install RVM  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
ENV PATH=$PATH:/usr/local/rvm/bin  
RUN rvm requirements  
RUN rvm install ruby-2.2  
RUN echo -e "\  
:update_sources: true\n\  
:sources:\n\  
\- http://gems.rubyforge.org/\n\  
\- http://gems.github.com\n\  
:benchmark: false\n\  
gem: --no-ri --no-rdoc\n" > .gemrc  
RUN rvm-exec 2.2 gem install bundler rake  

