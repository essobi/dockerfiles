FROM simonallier/sosie-exp-android-base  
MAINTAINER simon.allier@gmail.com  
  
RUN echo y | android update sdk --all --filter android-16 --no-ui --force  
WORKDIR /root  
RUN git clone https://github.com/github/android.git  
  
WORKDIR /root/android  
COPY pom.xml /root/android/pom.xml  
COPY build.sh /root/android/build.sh  
RUN sh build.sh  
  
WORKDIR /root/sosies-generator  
COPY exp.properties /root/sosies-generator/exp.properties  
COPY run.sh /root/sosies-generator/run.sh  
COPY dependencyPom.xml /root/android/dependencyPom.xml  

