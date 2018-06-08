FROM regexpress/base-maven:oraclejdk8  
  
ENV REPOSITORY=regexpress-flume  
ENV ARTIFACT=flume  
ENV BRANCH=1.6.0  
RUN cd /tmp && \  
wget https://github.com/rexpress/regexpress-common/archive/master.zip && \  
unzip master.zip && \  
mvn -f regexpress-common-master install && \  
rm -rf master.zip && \  
wget https://github.com/rexpress/$REPOSITORY/archive/$BRANCH.zip && \  
unzip $BRANCH.zip && \  
mvn -f $REPOSITORY-$BRANCH package && \  
rm -rf $BRANCH.zip && \  
mv $REPOSITORY-$BRANCH/target/lib /root && \  
mv $REPOSITORY-$BRANCH/target/$ARTIFACT-$BRANCH.jar /root && \  
rm -rf /tmp/* && \  
cd /root && \  
echo "arg=();for var in \"\$@\";do arg+=(\"\$(echo -n \"\$var\" | base64
-d)\"); done; java -jar /root/$ARTIFACT-$BRANCH.jar \"\${arg[@]}\"" > run.sh
&& \  
chmod 755 run.sh  
  
ENTRYPOINT ["/bin/bash", "/root/run.sh"]

