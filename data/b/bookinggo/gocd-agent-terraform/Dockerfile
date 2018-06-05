FROM gocd/gocd-agent-alpine-3.5:v17.10.0  
WORKDIR /  
  
COPY terraform-entrypoint.sh /terraform-entrypoint.sh  
  
ENV GIT_SSH_KEY ''  
ENV GIT_KNOWN_HOST ''  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
  
RUN chmod +x /terraform-entrypoint.sh  
RUN wget
https://releases.hashicorp.com/terraform/0.11.2/terraform_0.11.2_linux_amd64.zip  
RUN unzip /terraform_0.11.2_linux_amd64.zip  
RUN mv /terraform /usr/bin/.  
RUN chmod 775 /usr/bin/terraform  
RUN rm /terraform_0.11.2_linux_amd64.zip  
  
ENTRYPOINT ["/terraform-entrypoint.sh"]  

