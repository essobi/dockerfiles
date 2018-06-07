FROM mhart/alpine-node:8  
MAINTAINER Matteo Melani <m@ellipsis.ai>  
  
# Set Time so that the Container is in synch with the Host  
ENV TZ=America/Los_Angeles  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apk update  
  
# Install some basic tools  
RUN apk add --update bash curl openssl ca-certificates tar gzip openssh zip \  
git groff less  
  
# Install python  
RUN apk add --no-cache python3 \  
&& python3 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip3 install --upgrade pip setuptools boto3\  
&& rm -r /root/.cache  
  
# Install AWS CLI  
RUN pip3 install awscli  
  
# Make a User so it is easier to use the AWS CLI tools and env. variables  
ENV EL_HOME=/home/el  
RUN addgroup -S el && adduser -S -g el el  
RUN passwd -d -u el  
RUN echo "el ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers  
  
RUN npm install -g aws-es-kibana  
  
EXPOSE 9200  
USER el  
WORKDIR ${EL_HOME}  
ENTRYPOINT ["aws-es-kibana", "-b", "0.0.0.0", "--region", "us-east-1"]  
CMD []  

