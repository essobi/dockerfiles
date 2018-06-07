# Dockerfile for Powershell Empire  
# written by James Taliento  
#  
# build with the command:  
# Build:  
# docker build -t empire .  
#  
# Run:  
# docker run -it -p 80:80 -p 443:443 -p 8080:8080 -p 8081:8081 -v
~/Empire/tmp:/tmp -v ~/Empire/data:/opt/Empire/data/downloads empire  
#  
# then access http://localhost:8000 in your browser  
# MAINTAINER James Taliento, james@manipulatesecurity.com  
FROM debian:jessie  
  
# Install dependencies  
RUN apt-get update && apt-get upgrade -y && apt-get install \  
apt-utils \  
curl \  
python \  
python-pip \  
lsb-release \  
sqlite3 \  
git -y  
  
# Upgrade pip  
RUN pip install --upgrade pip  
  
# Install empire  
RUN cd /opt && \  
git clone https://github.com/EmpireProject/Empire.git && \  
cd Empire/setup && \  
sh -c /bin/echo -e "\r" | ./install.sh  
  
# Default / common ports used by Empire listeners. Modify as needed.  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8080  
EXPOSE 8081  
# Jump on in to Empire  
WORKDIR /opt/Empire  
ENTRYPOINT ./empire  

