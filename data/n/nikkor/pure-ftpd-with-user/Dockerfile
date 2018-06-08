FROM stilliard/pure-ftpd  
MAINTAINER Nikita Korotkih <nikita.korotkih@gmail.com>  
RUN apt-get install -y python python-pip  
RUN pip install pexpect  
ADD create-user.py /  
  
RUN python /create-user.py  
RUN pure-pw mkdb  

