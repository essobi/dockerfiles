# last build: 22-05-2018 11:25:23  
FROM debian:9.4  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
sudo systemd  
  
RUN apt-get install -y net-tools wget gnupg curl sudo openssh-server cron vim
netcat-traditional less  
  
RUN curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -v
12.21.26  
  
RUN rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  

