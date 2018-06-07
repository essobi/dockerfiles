# Inherit from Heroku's stack  
FROM heroku/jvm  
  
# Install Lein  
RUN mkdir -p /app/bin  
ADD ./lein.bash /app/bin/lein  
RUN chmod +x /app/bin/lein  
ENV PATH /app/bin:$PATH  
RUN ["lein", "-v"]  
  
# Run lein to cache dependencies  
ONBUILD COPY ["project.clj", "/app/user/"]  
ONBUILD RUN ["lein", "deps"]  
  
ONBUILD COPY . /app/user/  
ONBUILD RUN ["lein", "uberjar"]  

