FROM ubuntu:16.04  
RUN apt update -y && \  
apt install -y emacs-nox zsh mlocate git sudo net-tools  
  
COPY nginx_signing.key /root/nginx_signing.key  
RUN apt-key add /root/nginx_signing.key  
  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx\n deb-
src http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >>
/etc/apt/sources.list  
RUN apt update -y  
RUN apt install -y unit  
RUN apt install -y build-essential php-dev libphp-embed php7.0-mysql  
  
RUN apt install -y composer  
# CMD ["/bin/bash"]  
# CMD ["/usr/sbin/init"]  
CMD ["/usr/sbin/unitd", "--no-daemon"]  
# ENTRYPOINT ["/bin/bash"]  
# VOLUME /var/run  
# RUN sleep 3  
# CMD socat UNIX-LISTEN:/var/run/control.unit.sock -  
# CMD ["/usr/sbin/unitd", "--no-daemon"]  
# RUN chmod 755 /var/run/control.unit.sock  
# curl -X PUT -d @/root/json/start.json --unix-socket /run/control.unit.sock
http://localhost/

