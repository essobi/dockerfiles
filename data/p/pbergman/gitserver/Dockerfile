FROM debian:stable  
MAINTAINER Philip Bergman <philip@zicht.nl>  
  
RUN echo "deb http://ftp.nl.debian.org/debian/ stable main contrib non-free" >
/etc/apt/sources.list  
RUN apt-get update -q && apt-get upgrade -qy  
RUN apt-get install git dropbear gitweb lighttpd supervisor mc -qy  
  
RUN useradd --comment 'git server user' \--user-group --system --shell
/bin/bash --create-home --home-dir /home/git git  
  
RUN mkdir -p /home/git/repositories/  
RUN chmod 775 /home/git/repositories/  
RUN chown git.users /home/git/repositories/  
  
ADD config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD config/gitweb.conf /etc/gitweb.conf  
ADD config/lighttpd.conf /etc/lighttpd/lighttpd.conf  
  
RUN echo "root:123456789" | chpasswd  
RUN echo "git:12345679" | chpasswd  
  
EXPOSE 2222 8888  
CMD ["/usr/bin/supervisord"]  

