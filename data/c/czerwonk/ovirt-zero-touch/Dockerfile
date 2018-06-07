FROM golang  
  
ENV API_INSECURE false  
ENV DEBUG false  
RUN apt-get install -y git && \  
go get github.com/czerwonk/ovirt-zero-touch  
  
CMD ovirt-zero-touch -debug=$DEBUG -insecure=$API_INSECURE -api-url=$API_URL
-username=$API_USER -password=$API_PASS  
EXPOSE 11337  

