FROM minimumbuilds/minimum_python3:latest  
  
MAINTAINER Minimum Builds <minumumbuilds@gmail.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL Name=minimum_husk \  
Version=0.0.3 \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/minimumbuilds/minimum_husk.git" \  
org.label-schema.vcs-ref=$VCS_REF  
  
RUN mkdir /app  
COPY . /app/  
WORKDIR /app  
  
RUN apk add ca-certificates gcc musl-dev libffi-dev python3-dev openssl-dev
make libxml2-dev libxslt-dev \  
&& pip3 install -r requirements.txt  
  
ENTRYPOINT ["python3"]  
CMD ["husk.py"]  
  

