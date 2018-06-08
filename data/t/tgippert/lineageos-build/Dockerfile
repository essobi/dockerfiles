FROM tgippert/android-build:latest  
  
ARG LINEAGEOS_BRANCH  
ENV LINEAGEOS_BRANCH ${LINEAGEOS_BRANCH:-cm-14.1}  
# Install the repo command according to
https://wiki.lineageos.org/devices/t6/build#install-the-repo-command  
RUN curl https://storage.googleapis.com/git-repo-downloads/repo >
/usr/local/bin/repo \  
&& chmod a+x /usr/local/bin/repo  
  
# Initializing repo and fetching current branch $LINEAGEOS_BRANCH  
RUN mkdir -p /android/lineage \  
&& cd /android/lineage \  
&& echo Initialising repo for branch $LINEAGEOS_BRANCH \  
&& repo init -u https://github.com/LineageOS/android.git -b $LINEAGEOS_BRANCH
-q --depth=1 \  
&& (for i in {1..5}; do repo sync -c -q -j 8 --no-clone-bundle && break || (if
[ $i -ge 5 ]; then echo "error in repo sync" && exit 1; fi); done)  

