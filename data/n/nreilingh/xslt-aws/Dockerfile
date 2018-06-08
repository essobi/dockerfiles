FROM python:3.5.2  
MAINTAINER nreiling@bard.edu  
RUN pip install boto3==1.3.0 \  
&& wget https://bitbucket.org/awslabs/amazon-s3-bitbucket-pipelines-
python/raw/master/s3_upload.py \  
&& apt-get update \  
&& apt-get install -y xsltproc ruby-full \  
&& gem install rake \  
&& rm -rf /var/lib/apt/lists/*  

