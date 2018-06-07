FROM python:3.6-stretch  
  
RUN apt-get update && apt-get install -y awscli  
RUN pip install virtualenv  
  
ADD fetch_and_run.sh /usr/local/bin/fetch_and_run.sh  
RUN chmod 755 /usr/local/bin/fetch_and_run.sh  
  
ENV REQUIREMENTS=''  
ENV SCRIPT_PATH=''  
ENV SCRIPT_NAME=''  
ENV FUNCTION=''  
ENV ARGS=''  
ENV AWS_ACCESS_KEY_ID=''  
ENV AWS_SECRET_ACCESS_KEY=''  
ENV ID_RSA_BITBUCKET=''  
WORKDIR /tmp  
ENTRYPOINT ["/usr/local/bin/fetch_and_run.sh"]  

