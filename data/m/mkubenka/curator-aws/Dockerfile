FROM alpine:3.6  
RUN apk --update add \  
python \  
py-setuptools \  
py-pip \  
git \  
&& pip install boto3==1.4.7 \  
# https://github.com/elastic/curator/pull/1079  
&& pip install git+https://github.com/mkubenka/curator.git@feature/aws-sts \  
&& pip install requests-aws4auth==0.9 \  
&& apk del py-pip git \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /code  
  
USER nobody:nobody  
  
COPY curator_aws.py /code/curator_aws.py  
  
WORKDIR /code  
  
CMD ["python", "/code/curator_aws.py"]  

