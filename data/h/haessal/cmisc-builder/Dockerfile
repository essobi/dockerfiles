FROM debian:stable  
  
MAINTAINER haessal@mizutamauki.net  
  
ENV DEBCONF_NOWARNINGS yes  
  
WORKDIR /root  
  
# Install packages  
RUN \  
apt-get update && apt-get upgrade -y && \  
apt-get install -y --no-install-recommends gcc g++ make cmake lcov curl && \  
apt-get install -y git  
  
# Install Google test  
RUN \  
git clone \--depth=1 -b release-1.8.0 https://github.com/google/googletest.git
/usr/src/gtest  
RUN \  
cd /usr/src/gtest/ && cmake . && make && make install  
  
# Configure Lcov (enable branch coverage)  
RUN \  
cat /etc/lcovrc | \  
sed -e 's/#genhtml_branch_coverage = 1/genhtml_branch_coverage = 1/g' | \  
sed -e 's/lcov_branch_coverage = 0/lcov_branch_coverage = 1/g' > ./lcovrc.tmp
&& \  
mv ./lcovrc.tmp /etc/lcovrc  

