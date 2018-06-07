FROM openjdk  
LABEL Autor="esnegirov" Company="Slice"  
COPY Sample.java /sources/  
WORKDIR /sources  
RUN javac Sample.java  
RUN rm Sample.java  
ENTRYPOINT ["java","Simple"]

