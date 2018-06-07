FROM centos:centos7  
  
# Install the latest EPEL release RPM.  
# Then add the GPG keys to help verify packages and reduce errors(red) in the
output.  
# Update the system.  
# Perform clean-up.  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& rpm --import \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \  
&& yum -y update \  
&& yum clean all  
  
# Install Nginx.  
# Perform clean-up.  
# Move default configuration out of the way.  
RUN yum -y update \  
&& yum -y install nginx \  
&& yum clean all \  
&& mv /etc/nginx/nginx.conf /etc/nginx/nginx.txt  
  
# Add a custom nginx config  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./fastcgi_params /etc/nginx/fastcgi_params  
ADD ./generate-self-signed-cert.sh /bin/generate-self-signed-cert.sh  
ADD ./generate-named-ssl-cert.sh /bin/generate-named-ssl-cert.sh  
ADD ./start-nginx.sh /bin/start-nginx.sh  
  
RUN chmod a+x /bin/generate-self-signed-cert.sh  
RUN chmod a+x /bin/generate-named-ssl-cert.sh  
RUN chmod a+x /bin/start-nginx.sh  
RUN generate-self-signed-cert.sh  
  
EXPOSE 80  
EXPOSE 443  
# docker build --rm -t khalifahks/centos-nginx ./centos7-nginx  
# docker build --rm --no-cache -t khalifahks/centos-nginx ./centos7-nginx  
# docker run -d --rm -p 8081:80 -p 3443:443 --name centos-nginx -h
centos_nginx khalifahks/centos-nginx  
# docker run -it --rm -p 8081:80 -p 3443:443 --name centos-nginx -h
centos_nginx khalifahks/centos-nginx  
# docker exec -it centos-nginx bash  
ENTRYPOINT ["start-nginx.sh"]  

