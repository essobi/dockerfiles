FROM
ubuntu@sha256:0844055d30c0cad5ac58097597a94640b0102f47d6fa972c94b7c129d87a44b7  
#Ubuntu 14.04  
MAINTAINER Vict Tan <ychtan@email.gwu.edu>  
  
#This pre-fetches the most recent requirements.apt in dev.  
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-weibo-
datasts/dev/requirements/requirements.apt /opt/setup/  
RUN apt-get update  
RUN cat /opt/setup/requirements.apt | tr "\n" " " | xargs apt-get install -y  
RUN pip install pip==7.1.2  
  
#This pre-fetches the most recent requirements.txt.  
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-weibo-
datasts/dev/requirements/common.txt /opt/setup/  
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-weibo-
datasts/dev/requirements/requirements.txt /opt/setup/  
RUN pip install -r /opt/setup/requirements.txt  
  
#Install appdeps to allow checking for application dependencies  
RUN pip install appdeps  
  
#This is used to automatically create the admin user.  
RUN pip install django-finalware==0.1.0  
  
ADD invoke.sh /opt/  
RUN chmod +x /opt/invoke.sh  
  
WORKDIR /opt/sfm-weibo-datasts  
CMD ["/opt/invoke.sh"]  
EXPOSE 80

