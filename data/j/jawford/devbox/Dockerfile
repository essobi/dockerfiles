FROM ubuntu:14.04  
  
RUN apt-get update -y  
RUN apt-get install -y git  
RUN apt-get install -y python  
RUN apt-get install -y curl  
RUN apt-get install -y vim  
RUN apt-get install -y strace  
RUN apt-get install -y diffstat  
RUN apt-get install -y pkg-config  
RUN apt-get install -y cmake  
RUN apt-get install -y build-essential  
RUN apt-get install -y tcpdump  
RUN apt-get install -y screen  
  
# Setup home environment  
RUN useradd dev  
RUN mkdir /home/dev && chown -R dev:dev /home/dev  
RUN mkdir -p /home/dev/bin /home/dev/lib  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will belong to root.
This is probably a Docker bug.  
RUN mkdir -p /var/shared/RUN && touch /var/shared/placeholder  
RUN chown -R dev:dev /var/shared  
VOLUME /var/shared  
  
ENV PATH /home/dev/bin:$PATH  
ENV PKG_CONFIG_PATH /home/dev/lib/pkgconfig  
ENV LD_LIBRARY_PATH /home/dev/lib  
  
WORKDIR /home/dev  
ENV HOME /home/dev  
  
ADD vimrc /home/dev/.vimrc  
ADD vim /home/dev/.vim  
ADD bash_profile /home/dev/.bash_profile  
ADD profile /home/dev/.profile  
ADD gitconfig /home/dev/.gitconfig  
ADD bash_aliases /home/dev/.bash_aliases  
ADD bashrc /home/dev/.bashrc  
ADD scripts /home/dev/  
RUN echo done files and folders  
  
## Link in shared parts of the home directory  
## make symbolic links to these targets in the current directory  
## eg /home/dev/.ssh -> /var/shared/.ssh,  
## any writes to .ssh, history, will be placed on the volume, and may also be
shared by other containers  
RUN ln -s /var/shared/.ssh  
RUN ln -s /var/shared/.bash_history  
  
## Finally, as all files were created with uid gid of 0...  
RUN chown -R dev:dev /home/dev  
  
## Default to a login shell  
USER dev  
  
## this doesn't seem to be necessary, and may be implied by the USER statement
above  
CMD ["/bin/bash", "--login"]  
  
## RELATED  
## docker build -t "my_image_repo_name_and_optional_tag" .  
## Provide access to the docker client binary, and the daemon socket by bind
mounting these files:  
## docker run  
## -it --rm  
## -v /Users:/Users  
## -v /var/run/docker.sock:/var/run/docker.sock  
## -v $(which docker):/bin/docker \  
## --name "devbox" \  
## "jawford/devbox:latest"  

