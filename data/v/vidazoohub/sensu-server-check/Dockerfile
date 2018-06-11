# using alpine because it's the smallest i can use  
FROM alpine:3.3  
# whoami  
MAINTAINER naor livne <naorlivne@gmail.com>  
  
# update the index so i can actully use it for something  
RUN apk update  
  
#install python & postfix  
RUN apk add python py-pip postfix  
  
#install the required python modules  
RUN pip install requests email  
  
# adding the codebase  
RUN mkdir /sensu-server-check  
COPY / /sensu-server-check/  
RUN chmod +x /sensu-server-check/sensu-server-check.py  
  
#setting python to run unbuffered for logs sake  
ENV PYTHONUNBUFFERED=1  
#changing rundir  
WORKDIR /sensu-server-check  
  
# and running it  
CMD postfix -c /etc/postfix/ start && python /sensu-server-check/sensu-server-
check.py  
  

