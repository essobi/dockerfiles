FROM mrupgrade/deadsnakes:3.3  
  
MAINTAINER MrUPGrade itsupgradetime@gmail.com  
  
RUN apt-get update && \  
apt-get -y install build-essential&& \  
apt-get -y install libffi-dev libssl-dev && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["python"]  

