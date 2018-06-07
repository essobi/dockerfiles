FROM alpine  
ADD ./srv /bin/srv  
RUN chmod a+x /bin/srv  
EXPOSE 8000  
ENTRYPOINT ["/bin/srv", "-p", "8000", "-u", "jetbrains"]

