FROM golang:1.7.3  
MAINTAINER mxpetit <maximepetit@hotmail.fr>  
  
# Get wait-for-it  
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh ./wait-for-it.sh  
RUN chmod +x ./wait-for-it.sh  
  
# Get migrate  
RUN go get -u github.com/mattes/migrate  
  
# Get cqlsh to create keyspace  
RUN apt-get update  
RUN apt-get install -y python3.4 python-pip netcat  
RUN pip install cqlsh==4.0.1  
  
# Add migrations files  
ADD migrations/ /go/  
ADD migrations.sh /go/  
RUN chmod +x /go/migrations.sh  
ADD keyspace.cql /go/  

