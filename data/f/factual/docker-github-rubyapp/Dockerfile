FROM phusion/passenger-ruby22  
  
RUN DEBIAN_FRONTEND=noninteractive; apt-get update; apt-get -y upgrade;  
  
RUN mkdir -p /home/app/webapp  
  
RUN rm -f /etc/service/nginx/down  
  
ADD nginx-default-site /etc/nginx/sites-available/default  
ADD ssh_config /root/.ssh/config  
ADD pull_app.sh /etc/my_init.d/001_git_pull_app  
  
EXPOSE 80  
  

