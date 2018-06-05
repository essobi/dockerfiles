FROM fedora  
RUN dnf -y -q update  
RUN dnf --assumeyes install make gcc-gnat gprbuild bitten-slave svn \  
valgrind mariadb-devel mariadb-server sqlite-devel postgresql-devel  
RUN dnf clean all  
RUN svn checkout svn://forge.ada-ru.org/matreshka/trunk/matreshka \  
/root/matreshka-trunk  
CMD bitten-slave --work-dir=/root --no-loop \  
http://forge.ada-ru.org/matreshka/builds  

