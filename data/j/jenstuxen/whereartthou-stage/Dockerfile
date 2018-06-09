FROM azul/zulu-openjdk-debian  
# this forces dpkg not to call sync() after package extraction and speeds up
install  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
# we don't need and apt cache in a container  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
RUN apt-get update && apt-get install -y git curl  
RUN git clone https://jenstuxen@bitbucket.org/jenstuxen/whereartthou.git
/whereartthou-master  
RUN cd /usr/local && curl -L -k -O https://dl.bintray.com/sbt/native-
packages/sbt/0.13.7/sbt-0.13.7.tgz && tar xvzf sbt-*.tgz && rm sbt*.tgz  
ENV PATH $PATH:/usr/local/sbt/bin  
EXPOSE 9000  
WORKDIR /whereartthou-master/play/where-art-thou  
RUN sbt clean stage  

