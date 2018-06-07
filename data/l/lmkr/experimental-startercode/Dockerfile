FROM java:8  
#WORKDIR dat100-testassignment/src/hib/dat100/testassignment  
#RUN javac dat100-testassignment/src/hib/dat100/testassignment/A.java  
#Must have COPY and WORKDIR in order to build successfully  
#The main purpose of a CMD is to provide defaults for an executing container.  
COPY . /usr/src/test  
WORKDIR /usr/src/test  
#RUN javac dat100-testassignment/src/hib/dat100/testassignment/A.java  
RUN javac -cp .:junit/junit-4.12.jar:junit/hamcrest-core-1.3.jar
dat100-testassignment/src/hib/dat100/testassignment/*.java  
#CMD ["java","-cp", ".:junit/junit-4.12.jar:junit/hamcrest-
core-1.3.jar:dat100-testassignment/src", "org.junit.runner.JUnitCore",
"hib.dat100.testassignment.TestA"]  
CMD ["java","-cp", ".:junit/junit-4.12.jar:junit/hamcrest-
core-1.3.jar:dat100-testassignment/src",
"hib.dat100.testassignment.TestRunner"]  
  
#FROM:  
#The FROM instruction sets the Base Image for subsequent instructions.  
#As such, a valid Dockerfile must have FROM as its first instruction.  
#The image can be any valid image – it is especially easy to start by pulling
an image from the Public Repositories.  
#FROM must be the first non-comment instruction in the Dockerfile.  
#FROM can appear multiple times within a single Dockerfile in order to create
multiple images. Simply make a note of the last image ID output by the commit
before each new FROM command.  
#The tag or digest values are optional. If you omit either of them, the
builder assumes a latest by default. The builder returns an error if it cannot
match the tag value.  
#FROM forms:  
#1.FROM <image>  
#2.FROM <image>:<tag>  
#3.FROM <image>@<digest>  
#COPY:  
#The COPY instruction copies new files or directories from <src> and adds them
to the filesystem of the container at the path <dest>.  
#COPY forms:  
#1. COPY <src>... <dest>  
#2. COPY ["<src>",... "<dest>"] (this form is required for paths containing
whitespace)  
#More detials from Reference:
https://docs.docker.com/engine/reference/builder/#copy  
#WORKDIR:  
#The WORKDIR instruction sets the working directory for any RUN, CMD,
ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile.  
#If the WORKDIR doesn’t exist, it will be created even if its not used in any
subsequent Dockerfile instruction.  
#WORKDIR form:  
#WORKDIR /path/to/workdir  
#More detials from Reference:
https://docs.docker.com/engine/reference/builder/#workdir  
#NOTE:  
#Don’t confuse RUN with CMD. RUN actually runs a command and commits the
result;  
#CMD does not execute anything at build time, but specifies the intended
command for the image.  

