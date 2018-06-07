# Inherit from Heroku's stack  
FROM heroku/cedar:14  
RUN mkdir -p /app/user  
WORKDIR /app/user  
  
ENV STACK "cedar-14"  
ENV HOME /app  
  
# Install the JDK  
RUN mkdir -p /app/.jdk  
ENV JAVA_HOME /app/.jdk  
RUN curl -s --retry 3 -L https://lang-
jvm.s3.amazonaws.com/jdk/cedar-14/openjdk1.8-latest.tar.gz | tar xz -C
/app/.jdk  
ENV PATH /app/.jdk/bin:$PATH  
  
RUN mkdir -p /app/.profile.d  
RUN echo "export PATH=\"/app/.jdk/bin:\$PATH\"" > /app/.profile.d/jvm.sh  

