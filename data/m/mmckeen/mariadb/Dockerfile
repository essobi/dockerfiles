FROM opensuse:tumbleweed  
MAINTAINER Matthew McKeen <matthew@mmckeen.net>  
  
RUN zypper -n ref  
RUN zypper -n up  
  
# install mariadb  
RUN zypper -n in mariadb  
  
# expose database port  
EXPOSE 3306  
# remember that mysql still has  
# to be configured before  
# this next command will work  
CMD ["/usr/bin/mysqld_safe"]  

