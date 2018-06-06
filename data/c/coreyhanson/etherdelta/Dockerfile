FROM coreyhanson/lamp-base as git  
LABEL maintainer "Corey Ryan Hanson"  
  
#Git install for stage 1 of image.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
--no-install-recommends -y \  
git \  
ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
#Clones EtherDelta website repository.  
RUN git clone https://github.com/etherdelta/etherdelta.github.io.git  
  
#Begins stage 2 of image.  
FROM coreyhanson/lamp-base  
  
#imports EtherDelta pages.  
COPY \--from=git /etherdelta.github.io/ /var/www/etherdelta.github.io/  
  
#Import scripts  
COPY start-etherdelta.sh /  
COPY create-user.sh /  
COPY modify-sudoers.sh /  
  
#Modifies configuration files.  
RUN sed 's/var\/www\/html/var\/www\/etherdelta.github.io/' <
/etc/apache2/sites-available/000-default.conf > /etc/apache2/sites-
available/etherdelta.github.io.conf && \  
sed -i.bak '/DirectoryIndex ind/ c\  
\\\tDirectoryIndex index_com.html\  
' /etc/apache2/mods-available/dir.conf && \  
chmod +x start-etherdelta.sh create-user.sh modify-sudoers.sh && \  
a2ensite etherdelta.github.io.conf && \  
a2dissite 000-default.conf  
  
#Creates unprivileged user and adds Apache privilages.  
ARG docker_root_pass=liopleurodon  
ARG docker_unprivileged_user=etherdelta  
ENV docker_unprivileged_pass=devin  
RUN /create-user.sh && \  
/modify-sudoers.sh && \  
rm /create-user.sh modify-sudoers.sh  
  
#Switches to unprivelaged user.  
USER $docker_unprivileged_user  
WORKDIR /home/$docker_unprivileged_user  
  
CMD /start-etherdelta.sh  

