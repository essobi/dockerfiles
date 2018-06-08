FROM photon  
MAINTAINER gowatana  
  
ENV HTTP_ROOT /www  
WORKDIR $HTTP_ROOT  
  
RUN tdnf install -y python3 iproute2 iputils  
  
RUN mkdir -p $HTTP_ROOT/cgi-bin  
COPY test.py $HTTP_ROOT/cgi-bin/  
RUN chmod +x $HTTP_ROOT/cgi-bin/test.py; cat -n $HTTP_ROOT/cgi-bin/test.py  
  
EXPOSE 80  
CMD ["/usr/bin/python3", "-m", "http.server", "--cgi", "80"]  
  

