  
FROM ubuntu:latest  
  
ARG CUSTOM_USER=user  
# install sudo  
RUN apt-get update \  
&& apt-get install sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
# create the user  
RUN useradd -m "$CUSTOM_USER" \  
&& adduser "$CUSTOM_USER" sudo \  
&& echo "$CUSTOM_USER ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
COPY files/ /  
  
ENV CUSTOM_USER $CUSTOM_USER  
WORKDIR "/home/$CUSTOM_USER"  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD "/bin/bash"  
  

