FROM python:3.6-alpine  
LABEL maintainer="Kilna kilna@kilna.com"  
RUN pip install python-lambda &&\  
mkdir /lambda  
COPY bin/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/lambda_*  
WORKDIR /lambda  
ONBUILD COPY . /lambda  
ONBUILD RUN pip install -r requirements.txt &&\  
if [[ -d .aws ]]; then cd ~; ln -s /lambda/.aws; fi  
ONBUILD VOLUME /lambda  

