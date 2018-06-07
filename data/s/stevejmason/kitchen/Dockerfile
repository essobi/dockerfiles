FROM ubuntu:14.10  
MAINTAINER Stephen J. Mason <hi@stephenmason.me>  
  
RUN apt-get update  
RUN apt-get install -y wget  
RUN apt-get install -y docker.io  
RUN apt-get install -y git  
RUN wget -O- https://www.opscode.com/chef/install.sh | bash -s -- -P chefdk  
  
# Gen UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
WORKDIR /tmp  
  
# Kitchen-Docker GEM  
RUN chef gem install kitchen-docker  
  
# Kitchen-EC2.. custom GEM  
ENV kitchenec2commit 6fb9047  
RUN git clone https://github.com/stevejmason/kitchen-ec2.git  
WORKDIR /tmp/kitchen-ec2  
RUN git checkout ${kitchenec2commit}  
RUN chef gem build kitchen-ec2.gemspec  
RUN chef gem install kitchen-ec2*.gem  
  
# Working DIR  
WORKDIR /kitchen  

