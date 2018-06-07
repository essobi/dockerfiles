# https://docs.docker.com/reference/builder/  
# NOTE dockerignore is ignored https://github.com/docker/docker/issues/9455  
  
FROM ensime/ci-server:v2.x  
MAINTAINER Sam Halliday, sam.halliday@gmail.com  
  
################################################  
# ENSIME Ivy / Coursier Cache  
RUN\  
cd /root &&\  
git clone --depth 1 \--branch 2.0 https://github.com/ensime/ensime-server.git
&&\  
cd ensime-server &&\  
echo "ensimeServerJars := Nil" > ensime.sbt &&\  
echo "ensimeServerProjectJars := Nil" >> ensime.sbt &&\  
for SCALA_VERSION in 2.10.6 2.11.11 2.12.3 ; do\  
sbt ++$SCALA_VERSION ensimeConfig ensimeConfigProject ;\  
done &&\  
cd /root &&\  
rm -rf /root/ensime-server &&\  
git clone --depth 1 \--branch 2.0 https://github.com/ensime/ensime-sbt.git &&\  
cd ensime-sbt &&\  
sbt updateClassifiers &&\  
cd /root &&\  
rm -rf /root/ensime-sbt &&\  
git clone --depth 1 https://github.com/fommil/stalagmite.git &&\  
cd stalagmite &&\  
for SCALA_VERSION in 2.11.11 2.12.3 ; do\  
sbt ++$SCALA_VERSION update ;\  
done &&\  
cd /root &&\  
rm -rf /root/stalagmite &&\  
git clone --depth 1 https://github.com/fommil/drone-dynamic-agents.git &&\  
cd drone-dynamic-agents &&\  
for SCALA_VERSION in 2.12.3 ; do\  
sbt ++$SCALA_VERSION update ;\  
done &&\  
cd /root &&\  
rm -rf /root/drone-dynamic-agents &&\  
rm -rf $HOME/.coursier/cache/v1/https/oss.sonatype.org  
  
################################################  
# Emacs build tool  
RUN cask upgrade-cask  

