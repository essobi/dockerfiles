FROM phusion/baseimage:0.9.18  
# we need python- for aws-cli, if nothing else. "update" hasn't been done in
the base container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
python=2.* python-pip openjdk-7-jre-headless  
RUN pip install --upgrade pip awscli  
  
CMD mkdir -p /opt/app  
  
ENV build_s3_bucket="BUCKET_NAME"  
ENV build_s3_key="BUCKET_KEY"  
# make sure volumes are the last thing done in their directory. otherwise
contents are discarded with a further file operation.  
VOLUME /opt/  
VOLUME /usr/src/app/  
CMD touch /phusion-ready  
  
# no matter the command, we wrap it with my_init, which gets the services
running.  
CMD /sbin/my_init -- bash -c "mkdir -p /opt/app && aws --region=us-east-1 s3
cp s3://${build_s3_bucket}/${build_s3_key} /opt/app/app.tgz && tar -C
/opt/app/ -xzvf /opt/app/app.tgz && bash /opt/app/run.sh"  
  

