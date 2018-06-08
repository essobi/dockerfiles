#  
# messengerX Dockerfile based XPush platform  
#  
# https://github.com/xpush/dockerfile/messengerx  
#  
FROM centos:centos6  
  
# Install packages  
RUN \  
yum -y update && \  
yum -y groupinstall "Development Tools"  
  
# install nginx  
RUN \  
echo -e "\  
[nginx]\n\  
name=nginx repo\n\  
baseurl=http://nginx.org/packages/centos/6/x86_64/\n\  
gpgcheck=0\n\  
enabled=1\n" >> /etc/yum.repos.d/nginx.repo  
  
RUN yum -y install nginx  
  
# tell Nginx to stay foregrounded  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Install Wordpress  
ADD https://github.com/xpush/messengerX/archive/master.zip
/usr/share/nginx/messengerx.zip  
RUN cd /usr/share/nginx/ && unzip messengerx.zip && rm -f messengerx.zip  
RUN mv /usr/share/nginx/html/5* /usr/share/nginx/messengerX-master/www  
RUN rm -rf /usr/share/nginx/html  
RUN mv /usr/share/nginx/messengerX-master/www /usr/share/nginx/html  
RUN rm -rf /usr/share/nginx/messengerX-master  
  
# Define default command.  
CMD ["nginx"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

