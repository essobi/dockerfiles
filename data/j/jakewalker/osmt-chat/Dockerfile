# Dockerfile, this is where all the commands are run before the container is  
# deployed. The last line is probably going to be the command the container  
# runs everytime it is booted. For example, running a Python file.  
# The FROM is which image to base the container on, Alpine is a super cut down  
# version of Linux so doesn't take up lots of resources. This is one somebody  
# has made which has Python built in.  
FROM frolvlad/alpine-python3  
  
# The VOLUME lets us share a bit of the virtual drive with the host server.  
# It is used here to keep data persistant over updates.  
VOLUME /opt/data  
  
# The COPY instruction copies the app folder from the template into the  
# container image. Here we are coping the app folder to the opt directory in
the  
# root of the container.  
COPY app/ /opt/  
  
# The WORKDIR instruction is a bit like the `cd` command.  
WORKDIR /opt/  
  
# The EXPOSE instruction exposes a port to the host.  
EXPOSE 6666  
# The CMD instruction tells Docker the command to run everytime the container  
# boots up.  
CMD ["python3", "-u", "server.py"]  

