# DeployR Dockerfile  
# Mount Points  
# /home/deployr/deployr/$DEPLOYR_VERSION/deployr/database MongoDB  
FROM comses/miracle-r  
  
ARG DEPLOYR_RSERVE_VERSION=7.4.2  
ARG DEPLOYR_RSERVE_PACKAGE=deployrRserve_$DEPLOYR_RSERVE_VERSION.tar.gz  
ARG DEPLOYR_VERSION=8.0.0  
ARG DEPLOYR_PACKAGE=DeployR-Open-Linux-$DEPLOYR_VERSION.tar.gz  
  
USER root  
WORKDIR /opt/  
RUN yum makecache && yum install -y java-1.8.0-openjdk-devel pcre-devel
bzip2-devel xz-devel psmisc initscripts which \  
python-devel python-pip \  
&& wget -q https://github.com/deployr/deployr-
rserve/releases/download/v$DEPLOYR_RSERVE_VERSION/$DEPLOYR_RSERVE_PACKAGE \  
&& R CMD INSTALL $DEPLOYR_RSERVE_PACKAGE && mkdir -p /home/comses/download \  
&& wget -q
http://deployr.revolutionanalytics.com/download/bundles/release/$DEPLOYR_PACKAGE
\  
&& tar zxf $DEPLOYR_PACKAGE -C /home/comses/download \  
&& rm -f $DEPLOYR_RSERVE_PACKAGE $DEPLOYR_PACKAGE && yum clean all  
  
COPY installDeployROpen.sh /home/comses/download/installFiles/  
  
RUN mkdir -p /miracle/projects && cd /home/comses/download/installFiles/ \  
# pip install hardcoded libraries for luxedemo -- can remove later  
&& chmod +x installDeployROpen.sh && pip install pymongo uuid bcrypt \  
&& chown -R comses: /home/comses /miracle/projects  
  
USER comses  
RUN cd /home/comses/download/installFiles && export
JAVA_HOME=/usr/lib/jvm/java \  
&& sh installDeployROpen.sh --no-ask --nolicense \  
&& ln -s /miracle/projects
/home/comses/deployr/$DEPLOYR_VERSION/deployr/external/data/public  
  
COPY startAll.sh /home/comses/  
  
USER root  
RUN chown -R comses: /home/comses/ \  
&& chmod a+rx /home/comses/startAll.sh \  
&& rm -rf /home/comses/download  
  
EXPOSE 8000 8006  
USER comses  
CMD ["/home/comses/startAll.sh"]  

