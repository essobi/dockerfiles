FROM circleci/node  
  
# Installing serverless framework  
RUN sudo npm update -g && \  
sudo npm install -g serverless  
  
# Installing serverless framework plugins  
RUN sudo npm install serverless-aws-documentation --seva-dev && \  
sudo npm install serverless-step-functions --save-dev && \  
sudo npm install serverless-python-requirements  
  
# Installing python3  
#RUN sudo apt-get update && \  
# sudo apt-get install python3 && \  
# sudo apt-get install python3-pip  
RUN sudo apt-get update -y && sudo apt-get install -yq wget build-essential
gcc zlib1g-dev  
  
WORKDIR /tmp/  
RUN wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz \  
&& tar zxf Python-3.6.1.tgz \  
&& cd Python-3.6.1 \  
&& ./configure \  
&& sudo make altinstall  
ENV PYTHONIOENCODING "utf-8"  
RUN sudo ln /usr/local/bin/python3.6 /usr/local/bin/python3  
RUN sudo ln /usr/local/bin/pip3.6 /usr/local/bin/pip3  
  
# Installing AWS client  
RUN sudo pip3 install awscli  
  
WORKDIR /  

