#Dockerfile to print HelloWorld using C runtime  
#GNU Compiler Collection (GCC) will be used as base image. GCC image has C
runtime built within it.  
FROM gcc:4.9  
#Metadata specifying an image maintainer  
LABEL maintainer dockeraspnet@contoso.com  
  
#Copy all the file from current directory of source to destination container's
/usr/src/myapp directory  
COPY . /usr/src/myapp  
  
#Sets the working directory  
WORKDIR /usr/src/myapp  
  
#Compiles the helloworld.c using gcc  
RUN gcc -o myapp helloworld.c  
  
#Runs the compiles program to output HelloWorld  
CMD ["./myapp"]  
  

