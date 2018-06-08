FROM ubuntu:16.04  
  
MAINTAINER Gas <gas.mailbox@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y vim htop wget git unzip software-properties-common curl
python python-dev python-distribute python-pip cron  
RUN pip install pymongo tornado  
  
  
RUN mkdir /analytics  
ADD ./ /analytics/  
WORKDIR /analytics  
  
EXPOSE 4001  
#CMD ["/bin/bash"]  
#CMD ["nginx", "-g", "daemon off;"]  
CMD ["/usr/bin/python", "./main.py", ">", "/var/log/python.log"]  

