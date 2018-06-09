# The MIT License (MIT)  
# Copyright (c) 2017 Mario Loriedo  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE  
# OR OTHER DEALINGS IN THE SOFTWARE.  
FROM maven:3.5-jdk-8 as BUILD_IMAGE  
COPY src /usr/src/osio-issues-monitor/src  
COPY pom.xml /usr/src/osio-issues-monitor  
RUN mvn -f /usr/src/osio-issues-monitor/pom.xml clean compile assembly:single  
  
FROM openjdk:8-jre  
WORKDIR /root/  
COPY \--from=BUILD_IMAGE /usr/src/osio-issues-
monitor/target/stats4osio-1.0.0-SNAPSHOT.jar .  
ENTRYPOINT ["java","-jar","stats4osio-1.0.0-SNAPSHOT.jar"]

