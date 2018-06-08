FROM angelrr7702/ubuntu-13.10-sshd  
RUN apt-get install -y supervisor  
RUN apt-get install -y telnet  
RUN mkdir -p /var/log/supervisor  
ADD https://raw2.github.com/gygelly/docker-
ubuntu-13.10-base/master/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
EXPOSE 22 9001  
CMD ["/usr/bin/supervisord"]  

