from debian:9  
RUN apt-get update && apt-get install -y \  
build-essential \  
gdb  
  
COPY crasher.cc /usr/local/src/crasher.cc  
  
RUN g++ -std=c++11 -lpthread -o /usr/local/bin/example_crasher
/usr/local/src/crasher.cc  
  
CMD ["gdb", "--return-child-result", "-ex", "run", "-ex", "bt", "-ex", "quit",
"--batch", "/usr/local/bin/example_crasher"]  

