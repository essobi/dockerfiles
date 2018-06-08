FROM centos:centos7  
MAINTAINER levm "av@levm.eu"  
RUN yum -y update && yum clean all  
RUN yum -y install epel-release && yum clean all  
RUN yum -y install nginx  
  
# Install Ansible  
RUN yum install git build-essential python-dev python-pip -y  
RUN pip install pelican Markdown  
  
# config nginx  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD conf.d /etc/nginx/conf.d  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN curl
https://git.centos.org/sources/httpd/c7/acf5cccf4afaecf3afeb18c50ae59fd5c6504910
\  
| tar -xz -C /usr/share/nginx/html \  
\--strip-components=1  
RUN sed -i -e 's/Apache/nginx/g' -e '/apache_pb.gif/d' \  
/usr/share/nginx/html/index.html  
  
VOLUME /etc/nginx/conf.d  
EXPOSE 80  
ENTRYPOINT ["nginx"]

