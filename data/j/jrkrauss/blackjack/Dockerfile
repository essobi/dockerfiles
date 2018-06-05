FROM openjdk:9-jdk  
RUN echo "Creating BlackJack directory"  
RUN mkdir /tmp/BlackJack  
RUN echo "Copying all the files"  
COPY . /tmp/BlackJack  
WORKDIR /tmp/BlackJack  
ENV CLASSPATH /tmp/BlackJack/src  
RUN echo "COMPILING ALL THE SOURCE FILES!"  
RUN javac -cp
resources/External_Libs/sqlite/*:resources/External_Libs/miglayout/*:src
src/com/eca/assignment/*/*.java  
CMD ["java", "-cp",
"resources/External_Libs/sqlite/*:resources/External_Libs/miglayout/*:src",
"com.eca.assignment.main.BJMain"]

