from ubuntu:12.04  
  
maintainer rockets fhw2000@hotmail.com'  
run apt-get update \  
&& apt-get install -y openjdk-7-jdk \  
&& apt-get install -y openssh-server \  
&& apt-get install -y stress \  
&& mkdir /var/run/sshd  
  
run echo 'root:docker-sharing' | chpasswd  
  
run sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
expose 22  
run apt-get update  
  
run DEBIAN_FRONTEND=noninteractive apt-get install -y -q curl python-all
python-pip wget  
  
run mkdir /opt/webapp  
  
copy ./docker-sharing.py /opt/webapp/  
  
copy ./Procfile /opt/webapp/  
  
copy ./requirements.txt /opt/webapp/  
  
workdir /opt/webapp  
  
run pip install -r requirements.txt  
  
expose 5000  
  
expose 5001  
  
cmd ["python", "docker-sharing.py"]  
  
copy ./run.sh /opt/webapp  
  
run chmod u+x /opt/webapp/run.sh  
  
env PATH /opt/webapp:$PATH  

