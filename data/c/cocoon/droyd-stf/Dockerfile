FROM openstf/stf  
  
USER root  
  
  
#  
# install dependencies (envsubst)  
#  
RUN sudo apt-get update && sudo apt-get install -y gettext  
  
#  
# install android tools  
#  
RUN sudo apt-get update && sudo apt-get install -y android-tools-adb android-
tools-fastboot  
  
# Set up insecure default key  
RUN mkdir -m 0750 /.android  
ADD files/certs/insecure_shared_adbkey /.android/adbkey  
ADD files/certs/insecure_shared_adbkey.pub /.android/adbkey.pub  
  
#  
# install rethinkdb ( ref: https://www.rethinkdb.com/docs/install/ubuntu/)  
#  
#RUN . /etc/lsb-release && \  
# echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo
tee /etc/apt/sources.list.d/rethinkdb.list &&\  
# wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
&& \  
# sudo apt-get update && sudo apt-get install -y rethinkdb  
#  
# process cluster webui  
EXPOSE 28015 29015 8080  
#  
# install honcho  
#  
RUN sudo apt-get install -y python-pip && \  
pip install honcho  
  
#  
# install droydrunner  
#  
RUN git clone
https://cocoon_bitbucket@bitbucket.org/cocoon_bitbucket/droyd.git /tmp/  
RUN cd /tmp && \  
pip install -r requirements_server.txt && \  
python setup.py install && \  
cp droydserver/droydserve.py /usr/local/bin/droydserve && \  
chmod +x /usr/local/bin/droydserve  
  
# add demo  
#ADD droydserver/demo /tests/demo  
EXPOSE 5000  
#WORKDIR /tests  
#USER stf  
VOLUME ["/data"]  
WORKDIR /data  
#CMD ["rethinkdb", "--bind", "all"]  
COPY files/ /data  
  
CMD ["honcho", "start"]  
  

