FROM ubuntu:latest  
Maintainer Matt Klich, Mike Risse  
  
# Build: docker build -t dockernotebook:latest .  
# Run: docker run -d -P dockernotebook:latest  
RUN apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends install --yes \  
python-pip  
  
ADD ./dockernotebook/ /opt/dockernotebook/  
ADD ./requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
  
EXPOSE 5000  
CMD python /opt/dockernotebook/index.py  
  

