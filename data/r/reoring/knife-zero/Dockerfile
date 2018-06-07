FROM ruby:2.3.3  
WORKDIR /chef  
  
RUN wget
https://packages.chef.io/files/stable/chefdk/1.2.22/ubuntu/16.04/chefdk_1.2.22-1_amd64.deb  
RUN dpkg -i chefdk_1.2.22-1_amd64.deb && rm chefdk_1.2.22-1_amd64.deb  
RUN echo "PATH=$PATH:/root/.chefdk/gem/ruby/2.3.0/bin" >> ~/.bashrc  
RUN chef gem install knife-zero  
  
ENTRYPOINT ["knife", "zero"]  

