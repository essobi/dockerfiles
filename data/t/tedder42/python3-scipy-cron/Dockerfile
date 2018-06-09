FROM phusion/baseimage:0.9.18  
# look for new versions here: https://github.com/phusion/baseimage-
docker/blob/master/Changelog.md  
# has 'python3', nothing linked to 'python'.  
# need gcc to compile psycopg2  
# env: http://askubuntu.com/a/506635/69983  
ADD get-pip.py /usr/src/get-pip.py  
ADD requirements.txt /usr/src/requirements.txt  
  
# neurodebian source and key: pandas, scipy, etc.  
# http://neuro.debian.net/pkglists/toc_pkgs_for_release_trusty.html  
# http://neuro.debian.net/pkgs/python3-pandas-lib.html  
##ADD neurodebian.sources.list
/etc/apt/sources.list.d/neurodebian.sources.list  
##RUN apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80
0xA5D32F012649A5A9  
# need python3-dev for any pip installs, basically. freetype, pkg-config are
for matplotlib  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y libpq-
dev python3-dev g++ libfreetype6-dev pkg-config libffi-dev build-essential
libssl-dev # "python3-pandas=0.17.*"  
## others: python3-scipy python3-pandas-lib python3-pandas  
RUN python3 /usr/src/get-pip.py && pip3 install "psycopg2>=2.6,<2.7" cython
"pandas>=0.18,<0.19" "scipy>=0.17.1,<0.18" awscli && LANG=en_US.UTF-8 pip
install --upgrade -r /usr/src/requirements.txt && python3 -m nltk.downloader
-d /usr/local/share/nltk_data wordnet punkt stopwords  
#RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove -y gcc  
# keep this for later pip work  
RUN ln -s /usr/bin/python3 /usr/bin/python  
  
RUN mkdir -p /opt/app  
VOLUME /opt/  
VOLUME /usr/src/app/  
  
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
  

