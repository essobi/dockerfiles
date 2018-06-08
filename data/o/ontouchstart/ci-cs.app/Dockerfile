FROM centos:latest  
RUN yum -y install docker  
RUN yum groups mark convert  
RUN yum -y groupinstall 'Development Tools'  
RUN yum -y install glibc-static  
RUN curl https://sh.rustup.rs -sSf > rustup_init.sh  
RUN chmod +x rustup_init.sh  
RUN ./rustup_init.sh -y  

