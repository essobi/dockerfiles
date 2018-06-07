FROM java:7  
COPY . /usr/src/myapp  
WORKDIR /usr/src/myapp  
RUN javac Echo.java  
EXPOSE 8000  
CMD ["java", "Echo"]  

