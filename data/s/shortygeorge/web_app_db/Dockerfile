FROM java:8  
VOLUME /tmp  
ARG JAR_FILE  
ADD ${JAR_FILE} SHORTYGEORGE.jar  
RUN bash -c 'touch /app.jar'  
#ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/SHORTYGEORGE.jar"]  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-Dspring.profiles.active=container","-jar","/SHORTYGEORGE.jar"]  
EXPOSE 8080  
#This tells Docker to:  
#Build an image starting with the Python 3.4 image.  
#Add the current directory . into the path /code in the image.  
#Set the working directory to /code.  
#Install the Python dependencies.  
#Set the default command for the container to python app.py.

