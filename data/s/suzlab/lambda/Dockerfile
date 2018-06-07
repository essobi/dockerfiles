FROM suzlab/awscli:latest  
  
RUN pip install python-lambda-local lambda-uploader  
  
WORKDIR /root  
  
COPY .bashrc.patch ./  
RUN patch .bashrc < .bashrc.patch  
RUN rm .bashrc.patch  
  
RUN git clone https://github.com/suz-lab/lambda.git  

