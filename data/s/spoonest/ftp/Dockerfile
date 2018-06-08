FROM spoonest/docker-pure-ftpd  
  
RUN apt-get update -y  
RUN apt-get install -y python python-pip  
RUN pip install pexpect  
ADD create-user.py /  
  
RUN python /create-user.py  
RUN pure-pw mkdb  

