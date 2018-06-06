FROM centos:latest  
MAINTAINER "Andrew Rynhard" <andrewrynhard@autonomy.io>  
RUN yum -y group install "Development Tools"  
RUN yum -y install sudo which  
RUN sed -i -e 's/Defaults requiretty.*/ #Defaults requiretty/g' /etc/sudoers  
RUN useradd -m -d /chief chief  
ADD bash_profile /chief/.bash_profile  
RUN chown chief:chief /chief/.bash_profile  
RUN echo "chief ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN curl
https://e82b27f594c813a5a4ea5b07b06f16c3777c3b8c.googledrive.com/host/0BwnS5DMB0YQ6bDhPZkpOYVFhbk0/musl-1.1.12/crossx86-x86_64-linux-
musl-1.1.12.tar.xz | tar -xJ --strip-components 1 -C /chief  
ONBUILD ADD build.sh /chief/build.sh  
ONBUILD RUN chown -R chief:chief /chief  
ONBUILD RUN chmod +x /chief/build.sh  
ONBUILD USER chief  
WORKDIR /chief  
CMD ["/chief/build.sh"]  

