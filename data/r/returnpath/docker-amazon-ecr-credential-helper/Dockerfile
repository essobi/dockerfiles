FROM golang:1.6  
RUN apt-get update && apt-get install -y \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/local/go/src/github.com/awslabs/amazon-ecr-credential-
helper/ \  
&& wget -O /usr/local/go/src/github.com/awslabs/amazon-ecr-credential-
helper/master.zip \  
\--no-check-certificate https://github.com/awslabs/amazon-ecr-credential-
helper/archive/master.zip  
  
WORKDIR /usr/local/go/src/github.com/awslabs/amazon-ecr-credential-helper/  
  
RUN unzip master.zip && \  
mv amazon-ecr-credential-helper-master/* . && \  
rm -rf amazon-ecr-credential-helper-master && \  
rm -f master.zip  
  
# To ensure that the host has the necessary files after the container runs the  
# user must mount one volume from the host  
# -v /usr/local/bin:/usr/local/go/src/github.com/awslabs/amazon-ecr-
credential-helper/bin/local  
CMD /usr/bin/make  

