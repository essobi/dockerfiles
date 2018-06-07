FROM dexec/base-jdk:1.0.1  
MAINTAINER andystanton  
ADD image-common /tmp/dexec/image-common  
VOLUME /tmp/dexec/build  
ENTRYPOINT ["/tmp/dexec/image-common/dexec-runtime.sh", "javac", "java",
".class"]  

