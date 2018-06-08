FROM muicoder/glibc  
  
ARG WORK=/opt  
  
ENV JAVA_HOME=$WORK/jdk  
ENV JRE_HOME=$JAVA_HOME/jre  
ENV CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib  
  
ENV PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH  
  
RUN JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=172 \  
JAVA_VERSION_BUILD=11 \  
JAVA_DOWNLOAD_ID=a58eab1ec242421181065cdc37240b08 \  
JAVA_PACKAGE=jdk \  
JAVA_JCE=unlimited && \  
mkdir -p $WORK && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/$JAVA_DOWNLOAD_ID/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
| tar -xzf - -C $WORK && \  
ln -s $WORK/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} $JAVA_HOME && \  
if [ "${JAVA_JCE}" == "unlimited" ]; then \  
echo "Installing Unlimited JCE policy" && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip -o
/tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip && \  
unzip /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip -d /tmp && \  
mv /tmp/UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}/*.jar
$JRE_HOME/lib/security; \  
fi && rm -rf /tmp/*  
  
CMD ["java", "-version"]  

