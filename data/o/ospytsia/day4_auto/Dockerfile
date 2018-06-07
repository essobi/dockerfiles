FROM openjdk  
LABEL author="ospytsia" company="Slice"  
copy Sample.java /opt/  
WORKDIR /opt  
RUN javac Sample.java  
RUN rm Sample.java  
CMD java Sample

