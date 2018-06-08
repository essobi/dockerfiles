FROM python:3.6  
# Install/update build dependencies  
RUN apt update \  
&& apt install -y build-essential \  
libldap2-dev \  
libsasl2-dev \  
&& pip install -U pip \  
setuptools \  
wheel  
  
# Install software  
WORKDIR /hgi-groups  
ADD . .  
RUN pip install -r requirements.txt  
  
# Start API server  
EXPOSE 5000  
CMD python -m api.main  

