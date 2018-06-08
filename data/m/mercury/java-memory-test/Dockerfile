FROM broadinstitute/gatk:4.0.0.0  
COPY ./MemoryTest.java /MemoryTest.java  
  
RUN mkdir /MemTest && cd /MemTest && javac /MemoryTest.java -d .  
  
ENV CLASSPATH /MemTest

