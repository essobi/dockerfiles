FROM elixir:1.5.1  
# Enable https PPAs  
RUN echo deb http://ftp.debian.org/debian jessie-backports main >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y apt-transport-https vim  
RUN apt-get -t jessie-backports install -y jq  
  
# Instruct Apt to fetch a recent Node.js install  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
RUN echo 'deb https://deb.nodesource.com/node_6.x jessie main' >
/etc/apt/sources.list.d/nodesource.list  
RUN echo 'deb-src https://deb.nodesource.com/node_6.x jessie main' >>
/etc/apt/sources.list.d/nodesource.list  
  
# Environment/Build Dependencies  
RUN wget -nv https://get.docker.com/builds/Linux/x86_64/docker-17.03.0-ce.tgz  
RUN tar -xz -C /tmp -f docker-17.03.0-ce.tgz  
RUN mv /tmp/docker/* /usr/bin  
RUN apt-get update && apt-get install -y nodejs unzip build-essential
libpython-dev  
RUN npm install -g webpack  
  
# Install AWS CLI  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -b /usr/local/bin/aws  
  
COPY . /root/devops  

