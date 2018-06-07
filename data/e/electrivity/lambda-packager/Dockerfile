FROM node:8.10  
ENV DEFAULT_USER=node  
  
COPY change-uid /usr/local/bin/change-uid  
RUN chmod +x /usr/local/bin/change-uid  
  
# Add a non root user  
# RUN useradd $DEFAULT_USER -m -d /home/$DEFAULT_USER/ -s /bin/bash  
# Create working directory  
RUN mkdir /src && chown $DEFAULT_USER:$DEFAULT_USER /src  
WORKDIR /src  
  
COPY /entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
COPY /cmd.sh /cmd.sh  
RUN chmod +x /cmd.sh  
CMD ["/cmd.sh"]

