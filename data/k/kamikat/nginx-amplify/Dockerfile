FROM nginx:latest  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y python curl apt-transport-https  
  
RUN unlink /var/log/nginx/access.log \  
&& unlink /var/log/nginx/error.log \  
&& touch /var/log/nginx/access.log \  
&& touch /var/log/nginx/error.log  
  
# Install nginx-amplify-agent with dummy API key  
ENV API_KEY get-your-api-key-from-nginx-amplify-dashboard  
RUN curl -L https://github.com/nginxinc/nginx-amplify-
agent/raw/master/packages/install.sh \  
| sed '/service amplify-agent start >/d' \  
| sh -s -- -y  
  
VOLUME /etc/amplify-agent  
  
COPY service.sh /run/service.sh  
ENTRYPOINT [ "/run/service.sh" ]  

