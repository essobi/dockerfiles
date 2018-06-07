FROM groonga/groonga:8.0.0  
RUN apk --no-cache add cmake  
WORKDIR /usr/src  
RUN mkdir -p hog  
WORKDIR hog  
ADD src ./src  
ADD CMakeLists.txt ./  
ADD cmake ./cmake  
RUN cmake .  
RUN make all install  
WORKDIR ..  
RUN rm -rf hog  
  
EXPOSE 18618  
ENTRYPOINT ["hog"]  

