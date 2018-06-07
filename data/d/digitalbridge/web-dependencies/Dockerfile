FROM trzeci/emscripten:sdk-tag-1.36.6-64bit  
MAINTAINER Jay Faulkner  
  
ENV BOOST=1.59.0 BOOST_ZIP=1_59_0  
ENV EIGEN=3.2.10 EIGEN_ZIP=b9cd8366d4e8  
  
# swap out sh for bash to make life in general easier ...  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# fetch apt dependencies  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends wget build-essential cmake git-
core ca-certificates python2.7 python-pip  
  
# fetch AWS and AWS elastic beanstalk tools  
RUN pip install awscli awsebcli  
  
# fetch web dependencies  
RUN apt-get install -y --no-install-recommends nodejs npm mongodb ruby-compass
\  
&& rm -rf /var/lib/apt/lists/*  
RUN npm install -g bower grunt forever  
  
# build folder structure  
RUN mkdir /opt/dependencies  
  
# fetch boost  
RUN echo "fetching Boost ${BOOST} ..." \  
&& wget -P /opt/dependencies/
http://sourceforge.net/projects/boost/files/boost/${BOOST}/boost_${BOOST_ZIP}.tar.gz
\  
&& echo "extracting boost ..." \  
&& cd /opt/dependencies/ \  
&& tar xvf /opt/dependencies/boost_${BOOST_ZIP}.tar.gz --directory
/opt/dependencies/  
  
# fetch eigen  
RUN echo "fetching Eigen ${EIGEN} ..." \  
&& wget -P /opt/dependencies/
http://bitbucket.org/eigen/eigen/get/${EIGEN}.tar.gz \  
&& mv /opt/dependencies/${EIGEN}.tar.gz
/opt/dependencies/eigen_${EIGEN}.tar.gz \  
&& echo "extracting eigen ..." \  
&& cd /opt/dependencies/ \  
&& mkdir eigen \  
&& tar xvf /opt/dependencies/eigen_${EIGEN}.tar.gz --directory
/opt/dependencies/ \  
&& mv eigen-eigen-${EIGEN_ZIP} eigen/eigen3  
  
# tidy up  
RUN rm /opt/dependencies/*.tar.gz  
  
# alias ll because it's driving me crazy not having it  
RUN echo alias ll=\"ls -lah\" >> /root/.bashrc  

