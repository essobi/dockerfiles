#  
# paws dockerfile  
#  
# Build:  
# sudo docker build -t paws:latest -f Dockerfile-latest .  
#  
# Run:  
# sudo docker run -it --name paws-latest \  
# -v /home/<user>/github/ws/:/home/paws/paws paws:latest bash  
#  
FROM python:2  
RUN apt-get -qq update  
RUN apt-get install -y libvirt-dev  
RUN pip install --no-cache-dir paws-cli  
RUN adduser --disabled-password --uid 1000 --gecos "" paws  
USER paws  

