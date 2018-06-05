FROM jessewei/alpine-bash  
COPY app.bin /src/app.bin  
WORKDIR /src  
RUN chmod +x app.bin  
EXPOSE 80  
CMD ["./app.bin"]

