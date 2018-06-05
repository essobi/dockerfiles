FROM openjdk:8  
RUN mkdir -p /usr/local/algs4  
RUN chmod 755 /usr/local/algs4  
WORKDIR /usr/local/algs4  
  
RUN wget http://algs4.cs.princeton.edu/code/algs4.jar  
RUN wget http://algs4.cs.princeton.edu/linux/javac-algs4  
RUN wget http://algs4.cs.princeton.edu/linux/java-algs4  
RUN chmod 755 javac-algs4 java-algs4  
RUN mv javac-algs4 /usr/local/bin  
RUN mv java-algs4 /usr/local/bin  
  
RUN wget http://algs4.cs.princeton.edu/linux/checkstyle.zip  
RUN wget http://algs4.cs.princeton.edu/linux/checkstyle-algs4.xml  
RUN wget http://algs4.cs.princeton.edu/linux/checkstyle-suppressions.xml  
RUN wget http://algs4.cs.princeton.edu/linux/checkstyle-algs4  
RUN unzip checkstyle.zip  
RUN chmod 755 checkstyle-algs4  
RUN mv checkstyle-algs4 /usr/local/bin  
  
RUN wget http://algs4.cs.princeton.edu/linux/findbugs.zip  
RUN wget http://algs4.cs.princeton.edu/linux/findbugs.xml  
RUN wget http://algs4.cs.princeton.edu/linux/findbugs-algs4  
RUN unzip findbugs.zip  
RUN chmod 755 findbugs-algs4  
RUN mv findbugs-algs4 /usr/local/bin  
  
RUN curl -LO https://github.com/google/google-java-
format/releases/download/google-java-format-1.3/google-java-format-1.3-all-
deps.jar  
  
RUN echo "#! /bin/bash\njava -jar /usr/local/algs4/google-java-format-1.3-all-
deps.jar \$@" > java-format  
RUN chmod 755 java-format  
RUN mv java-format /usr/local/bin  
  
RUN groupadd --system --gid 1000 worker \  
&& useradd --system --gid worker --uid 1000 --shell /bin/bash --create-home
worker  
USER worker  
WORKDIR /home/worker  
  

