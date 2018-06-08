FROM debian:jessie  
  
MAINTAINER Alexander Mustafin <mustafin.aleksandr@gmail.com>  
  
# explicitly set user/group IDs  
RUN groupadd -r yeti-web --gid=999 && useradd -r -g yeti-web --uid=999 yeti-
web  
  
#Add repo  
RUN echo 'deb http://pkg.yeti-switch.org/debian/jessie stable main ext' >>
/etc/apt/sources.list && \  
echo 'deb http://nginx.org/packages/debian/ jessie nginx' >>
/etc/apt/sources.list  
  
#Grab keys and install packages  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 9CEBFFC569A832B6 && \  
apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 && \  
apt-get update && apt-get -y install yeti-web  
  
#Clean nginx configs  
RUN rm -f /etc/nginx/conf.d/*.conf  
  
EXPOSE 80 443 6666  
ENTRYPOINT ["/bin/bash"]  

