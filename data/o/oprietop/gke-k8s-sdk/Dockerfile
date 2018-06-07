FROM google/cloud-sdk:alpine  
MAINTAINER Oscar Prieto <oscarmpp@gmail.com>  
  
# Fetch and install the latest terraform binary  
RUN curl -s https://www.terraform.io/downloads.html | sed -n
"s@.*\"\\(.\\+linux_amd64.zip\\)\".*@\1@p" | xargs curl -O  
RUN unzip terraform_*zip  
RUN mv terraform /usr/local/bin  
RUN chmod +x /usr/local/bin/terraform  
RUN rm terraform_*zip  
  
# Install kubectl  
RUN gcloud components install kubectl  
  
# Copy our wrapper  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
ENTRYPOINT ["/usr/local/bin/run.sh"]  

