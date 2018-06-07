FROM centos:latest  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum -y install bash-completion  
RUN yum -y install make  
RUN yum -y install gcc  
RUN yum -y install gcc-c++  
RUN yum -y install wget  
RUN yum -y install vim  
RUN yum -y install ncurses-devel  
RUN yum -y install openssl-devel  
RUN yum -y install openssl  
RUN yum -y install git  
WORKDIR /usr/local/  
RUN git clone https://github.com/tagomoris/xbuild.git  
ADD ./vimrc /root/.vimrc  
RUN vim -u /root/.vimrc -i NONE -c "try | NeoBundleUpdate! | finally | q! |
endtry" -e -s -V1 || vim -u /root/.vimrc -i NONE -c "try | NeoBundleUpdate! |
finally | q! | endtry" -e -s -V1  

