FROM openjdk:7-alpine  
  
RUN wget -O /tmp/dirbuster.tar.bz2
https://downloads.sourceforge.net/project/dirbuster/DirBuster%20%28jar%20%2B%20lists%29/0.12/DirBuster-0.12.tar.bz2?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fdirbuster%2Ffiles%2FDirBuster%2520%2528jar%2520%252B%2520lists%2529%2F0.12%2F  
RUN tar xvjf /tmp/dirbuster.tar.bz2 && rm /tmp/dirbuster.tar.bz2  
  
WORKDIR "/DirBuster-0.12"  
ENTRYPOINT ["java", "-jar", "DirBuster-0.12.jar", "-H"]  

