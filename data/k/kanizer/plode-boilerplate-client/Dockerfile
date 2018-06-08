#  
# Nginx Dockerfile  
#  
# Pull base image.  
FROM codekoalas/nginx-node  
  
# Copy config over  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Copy files over  
COPY . /usr/src/project  
  
# Install Nginx and Vim.  
RUN \  
apt-get update && \  
apt-get install -y vim && \  
if test -d /usr/src/project; then echo "exist"; fi || mkdir /usr/src/project
&& \  
cd /usr/src/project && \  
npm i -g n && n 9 && exec $SHELL && \  
npm i -g npm && node -v && npm -v && \  
npm i && npm run build && \  
cd /var && rm -rf www/project/* && \  
cp -a ../../usr/src/project/dist/. www/project/  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["nginx", "-g", "daemon off;"]  
  
# Expose ports.  
EXPOSE 8080  
# docker build -t [user]/[image-name] .  
# docker run -p 5000:8080 --name [container-name] -dit [user]/[image-name]
nginx -g 'daemon off;'  
# docker commit -m 'comment' -a 'username' [container-id] [image-name]:[tag-
id]  
# docker push [username]/[image-name]  

