FROM node:6.10  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update && apt-get install -y python-dev \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
# AWS CLI  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \  
python get-pip.py && \  
pip install awscli  
  
# yarn  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
  
# firebase-tool  
RUN npm install -g firebase-tools  

