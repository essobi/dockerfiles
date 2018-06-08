ARG DIST_TAG=xenial  
FROM i386/ubuntu:$DIST_TAG  
  
RUN apt-get update && \  
apt-get install -y make git texlive-full texlive-lang-czechslovak && \  
apt-get clean  
  
# ADD /build /build  
# WORKDIR /build  
  
ENV THREADS=2  
  
ARG DIST_TAG  
ENV DIST_TAG $DIST_TAG  
  
ENV DIST_VER=1  
  
ENTRYPOINT latex -v && \  
pwd && \  
ls -la && \  
rm -rf output/* && \  
mkdir output/_html && \  
mkdir output/_pdf && \  
ls -la output && \  
git clone https://github.com/RoboticsBrno/RobotikaBrno-guides.git && \  
cd RobotikaBrno-guides && \  
git checkout RoboticsManual && \  
cd RoboticsManual && \  
make && \  
cp -r _html ../../output && \  
cp -r _pdf ../../output && \  
cd .. && \  
cd .. && \  
pwd && \  
ls -la /output && \  
ls -la /output/_html && \  
ls -la /output/_pdf && \  
echo "Finish"  
  
VOLUME /output  

