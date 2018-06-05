# The base image is alpine  
FROM alpine  
  
# Update and install packages  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
  
# Download terraform  
RUN wget --no-check-certificate
https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip  
  
# Extract terraform  
RUN unzip terraform_0.11.3_linux_amd64.zip  
  
# Move terraform binary to /usr/bin  
RUN mv terraform /usr/bin/  
  
# Download awless  
RUN wget --no-check-certificate
https://github.com/wallix/awless/releases/download/v0.1.10/awless-
linux-386.tar.gz  
  
# Extract awless  
RUN tar -xvf awless-linux-386.tar.gz  
  
# Move awless binary to /usr/bin  
RUN mv awless /usr/bin/  
  
# Clean up  
RUN rm terraform_0.11.3_linux_amd64.zip  
RUN rm awless-linux-386.tar.gz  
  
CMD ["terraform", "version"]  

