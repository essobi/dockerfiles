# See https://github.com/jupyter/docker-stacks  
FROM jupyter/minimal-notebook  
MAINTAINER VDA-LAB  
  
RUN pip install pymongo  
  
ADD students_2016.txt students.txt  
ADD pymongo_exercises.ipynb pymongo_exercises.ipynb  
ADD make-student-notebook.sh make-student-notebook.sh  
  
USER root  
RUN chmod a+x make-student-notebook.sh  
USER jovyan  
  
# Create a directory for each student  
# RUN cat /tmp/students.txt | xargs -n 1 mkdir  
# Create the student notebooks with a script  
RUN cat students.txt | xargs -n 1 ./make-student-notebook.sh  
  
# Clean up added files  
RUN rm students.txt  
RUN rm pymongo_exercises.ipynb  
RUN rm make-student-notebook.sh

