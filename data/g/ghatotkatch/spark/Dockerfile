FROM gettyimages/spark  
MAINTAINER Shreyas Kulkarni  
  
# OpenSSH connection is needed for spark master to talk to workers  
# we also need git and vim  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq -y install openssh-server git
vim wget apt-transport-https  
  
# install sbt and try to download all it's deps  
RUN echo "deb https://dl.bintray.com/sbt/debian /"
>>/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq -y install sbt \  
&& sbt about \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install conscript and giter8  
RUN curl https://raw.githubusercontent.com/n8han/conscript/master/setup.sh |
sh \  
&& /root/bin/cs n8han/giter8  
  
# set PATH to include /root/bin since that's where many scala tools will be
resting (cs, g8 etc)  
ENV PATH "$PATH:/root/bin"  
# start openssh server  
#RUN service ssh start  
#generate a local key  
RUN ssh-keygen -t rsa -b 2048 -C spark_local -N '' -f ~/.ssh/local \  
&& cp ~/.ssh/local.pub ~/.ssh/authorized_keys  
  
# start ssh-agent and load the local key  
#RUN echo "#!/bin/bash" >~/.ssh/sshagent.$(hostname) \  
# && ssh-agent >>~/.ssh/sshagent.$(hostname) \  
# && . ~/.ssh/sshagent.$(hostname) \  
# && ssh-add ~/.ssh/local  
# setup our bootstrap for entrypoint  
COPY bootstrap /usr/local/bin/start.spark  
RUN chmod +x /usr/local/bin/start.spark  
  
# setup spark env  
RUN cp /usr/spark/conf/spark-env.sh.template /usr/spark/conf/spark-env.sh \  
&& echo "export SPARK_EXECUTOR_INSTANCES=2" >>/usr/spark/conf/spark-env.sh \  
&& echo "export JAVA_HOME=/usr/java" >>/usr/spark/conf/spark-env.sh  
  
# export master and worker webui ports  
EXPOSE 8080 4040  
EXPOSE 8081 8082 8083 8084  

