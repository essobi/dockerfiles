FROM axeclbr/java:jdk7  
  
MAINTAINER axeclbr <axeclbr@posteo.de>  
  
COPY sbt /root/bin/sbt  
RUN chmod u+x $HOME/bin/sbt  
ENV PATH="$PATH:/root/bin"  
RUN apt-get update && apt-get install -y \  
curl \  
&& curl -L "https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/0.13.9/sbt-launch.jar" -o /root/bin/sbt-launch.jar \  
&& apt-get -y remove curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME ["$HOME/.m2", "$HOME/.ivy2", "$HOME/.sbt", "$HOME/workdir"]  
  
WORKDIR /root/workdir  
  
CMD ["/root/bin/sbt"]  

