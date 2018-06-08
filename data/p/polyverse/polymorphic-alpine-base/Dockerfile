FROM alpine  
  
ADD rescramble.sh /polyverse/  
  
ARG POLYVERSE_POLYMORPHIC_LINUX_KEY  
ENV POLYVERSE_POLYMORPHIC_LINUX_KEY
${POLYVERSE_POLYMORPHIC_LINUX_KEY:-czcw7pjshny8lzzog8bgiizfr}  
  
# Rescramble base  
RUN /polyverse/rescramble.sh  
  
# Rescramble when inheritor builds  
ONBUILD RUN /polyverse/rescramble.sh  
  

