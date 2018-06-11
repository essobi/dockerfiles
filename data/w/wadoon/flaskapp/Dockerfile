# Docker Image for Flask Applications  
# - no database or any other server  
# - just simple python and pip with flask and gunicorn  
#  
# VERSION 0.1  
#  
#  
FROM wadoon/python  
MAINTAINER Alexander Weigl <Alexander.Weigl@student.kit.edu>  
  
RUN pip install Flask gunicorn  
  
ENTRYPOINT [ "gunicorn", "-c", "/etc/gunicorn.cfg" ]  

