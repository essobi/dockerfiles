FROM google/python  
  
RUN pip install awscli  
ADD elb-presence /bin/elb-presence  
  
ENTRYPOINT ["/usr/bin/python"]  
CMD ["/bin/elb-presence"]  

