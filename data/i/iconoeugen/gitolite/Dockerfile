FROM centos:7  
MAINTAINER Horatiu Eugen Vlad "horatiu@vlad.eu"  
RUN yum -y install epel-release && \  
yum -y install httpd git gitweb gitolite3 nss_wrapper gettext && \  
yum clean all  
  
# Generic environment  
ENV USER apache  
ENV HOME /var/lib/gitolite3  
  
# Gitolite Admin credentials  
ENV ADMIN_USER="admin" \  
ADMIN_PASS="password"  
RUN sed -e "s/Listen 80.*/Listen 8080/" -i /etc/httpd/conf/httpd.conf && \  
for dir in ${HOME}/.ssh ${HOME} /var/log/httpd /run/httpd; do \  
mkdir -v -p ${dir} && chmod -cR g+rwX ${dir} && chgrp -cR 0 ${dir} ; \  
done && \  
chmod g+rw /etc/gitweb.conf  
  
COPY passwd.in /usr/share/gitolite3/passwd.in  
COPY config/git.conf /etc/httpd/conf.d/git.conf  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chown apache:root /entrypoint.sh \  
&& chmod ug+x /entrypoint.sh  
  
# Fix for logging on Docker 1.8 (See Docker issue #6880)  
RUN mkfifo -m 666 /var/log/httpd/access_log \  
&& mkfifo -m 666 /var/log/httpd/error_log  
# Disabled as it doesn't work with docker 1.8  
# forward request and error logs to docker log collector  
#RUN ln -sf /dev/stdout /var/log/httpd/access.log \  
# && ln -sf /dev/stderr /var/log/httpd/error.log  
USER ${USER}  
WORKDIR ${HOME}  
  
EXPOSE 8080  
CMD [ "/entrypoint.sh" ]  

