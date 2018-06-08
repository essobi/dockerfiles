FROM hashicorp/terraform:0.9.6  
ENV SHUSH_VERSION 1.3.1  
WORKDIR /root/app  
  
RUN curl -sL -o /usr/local/bin/shush \  
https://github.com/realestate-com-
au/shush/releases/download/v${SHUSH_VERSION}/shush_linux_amd64 \  
&& chmod +x /usr/local/bin/shush  
  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  

