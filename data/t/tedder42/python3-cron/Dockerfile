FROM phusion/baseimage:0.9.18  
# look for new versions here: https://github.com/phusion/baseimage-
docker/blob/master/Changelog.md  
# has 'python3', nothing linked to 'python'.  
# need gcc to compile psycopg2  
# env: http://askubuntu.com/a/506635/69983  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
python3-pip awscli libpq-dev gcc  
RUN pip3 install "psycopg2>=2.6,<2.7"  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove -y gcc  
  
#RUN ln -s /usr/bin/python3 /usr/bin/python  
#RUN pip install awscli  
CMD mkdir -p /opt/app  
  
ENV build_s3_bucket="BUCKET_NAME"  
ENV build_s3_key="BUCKET_KEY"  
# make sure volumes are the last thing done in their directory. otherwise
contents are discarded with a further file operation.  
VOLUME /opt/  
VOLUME /usr/src/app/  
  
# no matter the command, we wrap it with my_init, which gets the services
running.  
CMD /sbin/my_init -- bash -c "mkdir -p /opt/app && aws --region=us-east-1 s3
cp s3://${build_s3_bucket}/${build_s3_key} /opt/app/app.tgz && tar -C
/opt/app/ -xzvf /opt/app/app.tgz && bash /opt/app/run.sh"  
  

