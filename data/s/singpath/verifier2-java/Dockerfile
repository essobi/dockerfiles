FROM java:8-jdk  
  
RUN mkdir -p /app/build/dist && \  
mkdir -p /app/build/tests && \  
mkdir -p /app/bin && \  
adduser --system --home /playground verifier  
  
ENV PATH="$PATH:/app/bin"  
ENV CLASSPATH="/app/lib/*:/app/build/dist"  
COPY ./lib /app/lib  
COPY ./src /app/src  
RUN javac -sourcepath /app/src -d /app/build/dist -g
/app/src/com/singpath/cli/Main.java  
RUN javac -sourcepath /app/src -d /app/build/dist -g
/app/src/com/singpath/server/Main.java  
  
COPY ./tests /app/tests  
RUN javac -sourcepath /app/tests -d /app/build/tests -g
/app/tests/com/singpath/TestSuite.java  
  
COPY ./bin /app/bin  
  
USER verifier  
WORKDIR /playground  
  
EXPOSE 5000  
CMD ["/app/bin/verify"]

