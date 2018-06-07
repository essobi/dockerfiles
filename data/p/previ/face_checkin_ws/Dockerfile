FROM maven:3-jdk-8  
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y libgomp1 git  
  
RUN mkdir /appl && \  
mkdir /appl/face_checkin_ws  
  
WORKDIR /appl/face_checkin_ws  
RUN git clone https://previ@bitbucket.org/enimakers/checkincommon.git  
RUN git clone https://previ@bitbucket.org/enimakers/checkintotemws.git  
RUN cd checkincommon/CheckInCommon && \  
mvn install && \  
cp ./target/*.jar ../../. && \  
cd ../../checkintotemws/CheckInTotemWS && \  
mvn install && \  
cp ./target/*.jar ../../. && \  
cd ../../ && \  
rm -rvf checkincommon && \  
rm -rvf checkintotemws  
  
EXPOSE 8888  
CMD ["java", "-jar", "CheckInTotemWS-0.0.1.jar"]  

