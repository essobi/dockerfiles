FROM governmentpaas/terraform:latest  
  
RUN apk add \--update curl \  
&& rm -rf /var/cache/apk/* \  
&& curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh  

