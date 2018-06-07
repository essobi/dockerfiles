FROM ubuntu:16.04  
# Install dependencies  
RUN apt-get update && apt-get install -y subversion apache2 libapache2-svn
apache2-utils  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Copy svn config  
RUN mv svn.conf /etc/apache2/sites-available/svn.conf  
#RUN mv envvars /etc/apache2/envvars  
# Make port 80 available to the world outside this container  
EXPOSE 80  
# Enable svn  
RUN a2ensite svn  
  
# svn file go here  
VOLUME ["/backup"]  
VOLUME ["/svn"]  
  
# Run app.py when the container launches  
CMD ["bash", "start.sh"]

