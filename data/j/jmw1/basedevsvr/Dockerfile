# Ubuntu 13.04 from Stackbrew  
# Version 1.0  
FROM stackbrew/ubuntu:13.10  
# Where OS Packages Are Located Ubuntu Website - Internet  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" >
/etc/opt/sources.list; apt-get update; echo "export HOME=/root\nexport
LD_LIBRARY_PATH=/opt/sqlite383/lib:/opt/gcc-4.8/lib64\nexport
LD_RUN_PATH=/opt/gcc-4.8/lib64\nexport GOROOT=/root/go\nexport
GOPATH=/root/go/bin\nalias l='ls -CF --color=auto --group-directories-
first'\nalias la='ls -A --color=auto --group-directories-first'\nalias ll='ls
-la --color=auto --group-directories-first'\nalias renv='. ~/.bashrc'\nalias
vrc='vi ~/.bashrc'\nalias hst='perl ~/hst.pl $@'\nalias komodo='komodo
&'\nPATH=/opt/perl-5.14.4/bin:/root/go/bin:/opt/python3.3.4/bin:/opt/sqlite383/bin:/opt/sqlite383/lib:/opt/python3.3.4/bin:/opt/python3.3.4/lib:/opt/python3.3.4/share:/opt/python3.3.4/include:/opt/Komodo/bin:/opt/redis286/bin:$PATH"
>> /root/.bashrc  
  
ENV HOME /root  
ENV LD_LIBRARY_PATH /opt/sqlite383/lib  
ENV GOROOT /root/go  
ENV GOPATH /root/go/bin  
  
#RUN apt-get update - "These Would Change Packages Everytime a new Image is
Built"  
#RUN apt-get install -y python3.3 aptitude  
# Have To Be On Seperate Lines  
# Built & Installed On My VM Host. tar.gz(s) of Installation Directory  
ADD http://localhost:8000/go.tar.gz /  
ADD http://localhost:8000/perl-5.14.4.tar.gz /  
ADD http://localhost:8000/python3.3.4.tar.gz /  
ADD http://localhost:8000/redis286.tar.gz /  
ADD http://localhost:8000/sqlite383.tar.gz /  
ADD http://localhost:8000/hst.pl /root/  
  
RUN tar -xvzf go.tar.gz; mv /go /root; rm go.tar.gz; tar -xvzf
perl-5.14.4.tar.gz; mv /perl-5.14.4 /opt; rm perl-5.14.4.tar.gz; tar -xvzf
python3.3.4.tar.gz; mv /python3.3.4 /opt; rm python3.3.4.tar.gz; tar -xvzf
redis286.tar.gz; mv /redis286 /opt/redis286; rm redis286.tar.gz; tar -xvzf
sqlite383.tar.gz; mv /sqlite383 /opt/sqlite383; rm sqlite383.tar.gz;  
  
VOLUME ["/opt/redis286/redis-data"]  
# Default Port(s)  
EXPOSE 6379  
EXPOSE 8000  

