From golang:1.9  
# Set up environment  
ENV AWS_CLI_VERSION 1.11.131  
ENV BOTO_VERSION 1.3.0  
# Install general tools  
RUN apt-get update  
RUN apt-get install -y curl git jq zip  
  
# Install NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get install nodejs  
  
# Install PIP  
RUN apt-get install -y python  
RUN apt-get install -y python-pip  
RUN pip install --upgrade pip  
  
# Install AWS tools  
# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8
correctly:  
ENV PYTHONIOENCODING=UTF-8  
RUN pip --no-cache-dir install awscli==${AWS_CLI_VERSION}  

