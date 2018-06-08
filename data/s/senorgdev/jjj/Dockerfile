FROM jenkins  
MAINTAINER Tony Lefebvre <tony.lefebvre@seniorgrowth.com>  
  
USER root  
  
RUN apt-get update &&\  
apt-get install -y \  
python-pip \  
python-psycopg2 &&\  
pip install --upgrade \  
pip \  
virtualenv \  
awsebcli &&\  
apt-get autoremove -y &&\  
apt-get clean  
  
  
#USER jenkins # drop back to the regular jenkins user - good practice  

