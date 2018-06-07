# Using Python 3 base image  
FROM python:3  
MAINTAINER Lucas Rouckhout lucas.rouckhout@gmail.com  
  
# Working directory  
WORKDIR /payup  
  
# Add all the files to the workdir.  
ADD . /payup  
  
# Install all the python requirements.  
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt  
  
# Runs on dockers port 80  
EXPOSE 80  
# Run the app.  
CMD ["python3", "website_payup/manage.py", "runserver"]

