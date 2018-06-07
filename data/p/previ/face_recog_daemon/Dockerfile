FROM maven:3-jdk-8  
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y libgomp1 git  
  
RUN mkdir /appl && \  
mkdir /appl/face_recog_daemon  
  
WORKDIR /appl/face_recog_daemon  
RUN git clone https://previ@bitbucket.org/enimakers/checkincommon.git  
RUN git clone https://previ@bitbucket.org/enimakers/checkfaceandrecognize.git  
RUN cd checkincommon/CheckInCommon && \  
mvn install && \  
cp ./target/*.jar ../../. && \  
cd ../../checkfaceandrecognize/CheckFaceAndRecognize && \  
mvn install && \  
cp ./target/*.jar ../../. && \  
cd ../../ && \  
rm -rvf checkincommon && \  
rm -rvf checkinfacerecognize  
  
CMD ["java", "-jar", "CheckFaceAndRecognize-0.0.1.jar"]  

