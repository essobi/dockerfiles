FROM atlassian/default-image:2  
  
RUN npm install \--global yarn  
RUN apt-get update && apt-get install -y python-dev  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install awscli  
  

