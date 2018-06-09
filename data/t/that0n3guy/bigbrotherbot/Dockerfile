FROM ubuntu  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# install B3  
RUN apt-get -y install python-pip python-dev build-essential libsqlite3-dev  
RUN pip install b3  
  
#  
ENTRYPOINT ["/usr/local/bin/b3_run"]  
CMD ["--help"]

