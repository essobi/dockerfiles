FROM saturnism/kotlin-native:0.7 AS build  
RUN mkdir -p /src  
ADD . /src  
RUN kotlinc /src/ -o /app -opt  
  
FROM gcr.io/distroless/cc  
COPY \--from=build /app.kexe /app  
ENTRYPOINT ["/app"]  

