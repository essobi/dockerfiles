FROM ubuntu:14.04  
RUN mkdir /root/.ssh  
  
RUN echo "ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDWNy7H9mlJQ6HvC7lfs7dU3FzWhFZeOaEe9VQzLfsPitz1IFCxkEteLM3b72paCmSk/bameNdVnsBbhHsK6d3aN2ioeB9BJuMYp6zJjCLq9f4s9t9CkG9lbs1hDzra1xU0La5eqQeQEGM1sJF1URotespJqUK/bGOnOdL9CVs9aQyUQV5xtQQt168haUqC+qIJODYl2DZ/6lLl/vEviYdxWRi4LESrYQUDMm/JwU65mXEjBNwtzz/Zi+4ySYHQbqcQ+tfYPCO+ldbWd9rz0asveV2hoSyoWUYJAxTBdKi8g7b37HYM09U5fNbDZC3cMmh4mA6bCxL6wpA+jgKosUmZ
php7@docker" > /root/.ssh/authorized_keys  
  
RUN locale-gen zh_CN.UTF-8  
  
RUN apt-get update  
  
RUN apt-get install git vim htop -y  
  
RUN apt-get install openssh-server python-software-properties software-
properties-common -y  
  
ENV LC_ALL="zh_CN.UTF-8"  
RUN add-apt-repository ppa:ondrej/php -y  
  
RUN apt-get update  
  
RUN apt-get install php7.0 php7.0-cli php7.0-json php7.0-pdo-mysql php-redis
-y  
  
RUN mkdir /var/run/sshd  
  
EXPOSE 22 80  
CMD ["/usr/sbin/sshd", "-D"]  

