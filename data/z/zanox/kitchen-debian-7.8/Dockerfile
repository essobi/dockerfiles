FROM debian:7.8  
RUN apt-get update  
RUN apt-get install -y net-tools  
RUN apt-get install -y curl sudo openssh-server cron vim netcat-traditional  
  
RUN curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -v
12.5.1

