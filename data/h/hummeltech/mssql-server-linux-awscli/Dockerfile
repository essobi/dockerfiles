FROM microsoft/mssql-server-linux:latest  
  
ENV SHELL=/bin/bash  
  
# Install build-essential, git, python-pip, libpython-dev, libyaml-dev, xz-
utils and awscli  
RUN apt-get update  
RUN apt-get install -y build-essential git python-pip libpython-dev libyaml-
dev xz-utils  
RUN pip install --upgrade --user awscli  
RUN echo 'eval $(grep -e aws_access_key_id -e aws_secret_access_key
~/.aws/credentials | sed "s/ //g" | sed "s/aws_access_key_id/export
AWS_ACCESS_KEY_ID/g" | sed "s/aws_secret_access_key/export
AWS_SECRET_ACCESS_KEY/g")' >> ~/.bashrc  
RUN rm -rf /var/lib/apt/lists/*  

