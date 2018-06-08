FROM militarycars/sugar-docker-amazon-linux-2-image  
LABEL author=magarenz@militarycars.com  
  
RUN adduser ec2-user  
  
COPY apps/sugarfixpermissions /usr/local/bin/sugarfixpermissions  
RUN chmod +x /usr/local/bin/sugarfixpermissions  
  
CMD ["/usr/local/bin/sugarfixpermissions"]

