FROM tutum/ubuntu:trusty  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -y \  
rsync \  
curl \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN sed -i "s/#PasswordAuthentication.*/PasswordAuthentication no/g"
/etc/ssh/sshd_config

