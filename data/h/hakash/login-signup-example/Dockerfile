FROM alpine  
  
#Add the needed software  
RUN apk add --no-cache git  
RUN apk add --no-cache openssh  
RUN apk add --no-cache nginx  
RUN apk add --no-cache shadow  
  
#Remove and replace the nginx.conf file  
RUN rm /etc/nginx/nginx.conf  
RUN printf "user nobody nogroup;\n\  
worker_processes 1;\n\  
daemon off;\n\  
error_log /dev/stderr info;\n\  
\n\  
events {\n\  
worker_connections 1024;\n\  
}\n\  
\n\  
http {\n\  
include mime.types;\n\  
\n\  
log_format main '$remote_addr - $remote_user [$time_local] \"$request\" '\n\  
'$status $body_bytes_sent \"$http_referer\" '\n\  
'\"$http_user_agent\" \"$http_x_forwarded_for\"';\n\  
\n\  
access_log /dev/stdout main;\n\  
\n\  
sendfile on;\n\  
tcp_nopush on;\n\  
\n\  
keepalive_timeout 65;\n\  
\n\  
gzip on;\n\  
\n\  
server {\n\  
listen 80;\n\  
root /website_files;\n\  
access_log /dev/stdout;\n\  
location / {\n\  
index index.html;\n\  
#try_files $uri $uri/ @notfound;\n\  
}\n\  
\n\  
location @notfound {\n\  
return 404;\n\  
}\n\  
}\n\  
\n\  
}" > /etc/nginx/nginx.conf  
  
RUN groupadd -g 9999 appuser && \  
useradd -r -m -u 9999 -g appuser appuser  
  
#Create needed directories for serving the files, storing the nginx.pid and
the SSH keys  
RUN mkdir /website_files  
RUN chown appuser /website_files  
  
RUN mkdir -p /run/nginx  
RUN chmod +w /run/nginx  
  
USER appuser  
  
  
RUN mkdir ~/.ssh  
  
#Fetch the public host key from github and add to the known hosts file  
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts  
  
#Add the deploy key to the ssh-agent for logging in on github  
RUN printf '-----BEGIN RSA PRIVATE KEY-----\n\  
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\n\  
\-----END RSA PRIVATE KEY-----\n\  
' > ~/.ssh/id_rsa && chmod 400 ~/.ssh/id_rsa  
#Set the current working directory  
WORKDIR /website_files  
  
#Start the ssh-agent and load the client key  
RUN eval $(ssh-agent) && \  
ssh-add ~/.ssh/id_rsa && \  
git clone git@github.com:hakash/login-signup-example.git .  
  
#Publish the webserver port  
EXPOSE 8080  
  
#Start Nginx  
ENTRYPOINT [ "nginx" ]  

