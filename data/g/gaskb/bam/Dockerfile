FROM ubuntu:16.04  
MAINTAINER Gas <gas.mailbox@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y vim htop wget git unzip software-properties-common curl
python python-dev python-distribute python-pip cron  
RUN pip install pymongo tornado  
  
ADD docker_files/cron_stats /etc/cron.d/cron_stats  
RUN chmod 0644 /etc/cron.d/cron_stats  
  
RUN touch /var/log/cron.log  
CMD cron && tail -f /var/log/cron.log  
  
RUN mkdir /analytics  
ADD ./ /analytics/  
WORKDIR /analytics  
  
ENV PYTHONPATH=/analytics/  
  
EXPOSE 4003  
#CMD ["/bin/bash"]  
#CMD ["nginx", "-g", "daemon off;"]  
CMD ["/usr/bin/python", "./main.py", ">", "/var/log/python.log"]  

