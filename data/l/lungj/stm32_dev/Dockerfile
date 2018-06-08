FROM ubuntu:zesty  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN apt-get install -y curl  
RUN apt-get install -y python3-pip  
RUN pip3 install cpplint  
RUN pip3 install pyyaml  
RUN apt-get install -y git flex bison cmake  
RUN cd opt && git clone https://github.com/doxygen/doxygen.git && cd doxygen
&& mkdir build; cd build && cmake -G "Unix Makefiles" .. && make && make
install  
RUN apt-get install -y default-jdk  
RUN pip3 install openpyxl  
RUN curl -o gcc-arm-none-eabi-7-2017-q4-major-linux.tar.bz2 -L
"https://developer.arm.com/-/media/Files/downloads/gnu-rm/7-2017q4/gcc-arm-
none-eabi-7-2017-q4-major-
linux.tar.bz2?revision=375265d4-e9b5-41c8-bf23-56cbe927e156?product=GNU%20Arm%20Embedded%20Toolchain,64-bit,,Linux,7-2017-q4-major"  
RUN bunzip2 gcc-arm-none-eabi-7-2017-q4-major-linux.tar.bz2  
RUN tar xvf gcc-arm-none-eabi-7-2017-q4-major-linux.tar  
RUN rm gcc-arm-none-eabi-7-2017-q4-major-linux.tar  
ENV PATH="/gcc-arm-none-eabi-7-2017-q4-major/bin/:${PATH}"  

