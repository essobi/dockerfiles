FROM pjzz/base  
  
# Install tahoe  
RUN apt-get install -y build-essential python-pip libcrypto++-dev python-dev
libssl-dev libffi-dev  
RUN pip install twisted && pip install allmydata-tahoe  
  
RUN mkdir -p /tahoe  
RUN chown -R daemon:daemon /tahoe  
  
RUN tahoe create-introducer /tahoe  
RUN echo "34567" > /tahoe/introducer.port  
EXPOSE 34567  
WORKDIR /tahoe  
ENTRYPOINT ["twistd"]  
CMD ["-ny", "tahoe-introducer.tac"]  

