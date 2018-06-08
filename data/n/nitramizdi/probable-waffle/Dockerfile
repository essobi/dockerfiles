# Use an official Python runtime as a parent image  
# Using someoneelse's image  
FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild  
  
#RUN apk update && \  
# apk add python3 apache2-mod-wsgi  
#ADD httpd.conf /usr/local/apache2/conf/httpd.conf # ADD from_this_dir
to_this_dir  
# Install any needed packages specified in requirements.txt  
#RUN pip install -r requirements.txt  
#RUN apt-get install -y apache2  
# Make port 50000 available to the world outside this container  
#EXPOSE 50000  
# Run app.py when the container launches  
CMD ["app.py"]  

