FROM ubuntu:16.04  
MAINTAINER Jan Drabek <drabek.honza@gmail.com>  
  
ENV APP_PATH="/home/drabekj/app"  
ENV AWS_ACCESS_KEY_ID="AKIAJJUCTSHV4DQBYIMQ"  
ENV AWS_SECRET_ACCESS_KEY="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"  
# Update system and install basic tools  
RUN apt-get update && apt-get install -y curl wget default-jre git python3-pip
vim  
  
# Setup user environment drabekj with root access  
#RUN adduser --home /home/drabekj --disabled-password --gecos '' drabekjls  
RUN useradd -m drabekj && adduser drabekj sudo  
#RUN adduser drabekj sudo  
RUN echo '%sudoers ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Switch to drabekj user  
USER drabekj  
  
  
# Set the working directory to /app  
WORKDIR ${APP_PATH}  
  
# Copy the current directory/src contents into the container at
/home/drabekj/app  
ADD ./src ${APP_PATH}/src  
ADD requirements.txt ${APP_PATH}  
# Set the owner of /home/drabekj/app to drabekj  
USER root  
RUN chown drabekj:drabekj ${APP_PATH}  
USER drabekj  
  
  
# Pip install any needed packages specified in requirements.txt  
RUN pip3 install -r ${APP_PATH}/requirements.txt  
  
# Make port 80 available to the world outside this container  
EXPOSE 3333  
# Run app.py when the container launches  
CMD ["python3", "src/app.py"]  

