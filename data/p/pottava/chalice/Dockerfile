# Chalice v0.0.1  
# Python Serverless Microframework for AWS  
# @see https://github.com/awslabs/chalice  
#  
# docker run --rm -v `pwd`:/app -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY
-e AWS_DEFAULT_REGION pottava/chalice  
# docker run --rm -v `pwd`:/app -v
$HOME/.aws/credentials:/root/.aws/credentials pottava/chalice  
#  
# docker run --rm -v `pwd`:/app -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY
-e AWS_DEFAULT_REGION pottava/chalice new-project hello  
# docker run --rm -v `pwd`:/app -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY
-e AWS_DEFAULT_REGION pottava/chalice deploy  
FROM pottava/python:2.7  
RUN apk --no-cache add --virtual build-dependencies curl py-pip \  
&& curl https://bootstrap.pypa.io/ez_setup.py | python \  
&& pip install virtualenv \  
&& pip install 'chalice == 0.0.1' \  
&& apk del build-dependencies  
  
WORKDIR /app  
VOLUME /app  
  
ENTRYPOINT ["/usr/bin/chalice"]  
CMD ["--help"]  

