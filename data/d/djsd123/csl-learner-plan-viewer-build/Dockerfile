FROM djsd123/csl-learner-plan-viewer-build:v2  
MAINTAINER Mikael Allison <mikael.allison@digital.cabinet-office.gov.uk>  
USER dev  
WORKDIR /home/dev/learner_plan_viewer/  
RUN git pull https://github.com/crossgovernmentservices/csl-learner-plan-
viewer.git  
RUN pip install -r /home/dev/learner_plan_viewer/requirements/dev.txt  
ONBUILD WORKDIR /home/dev/learner_plan_viewer/  
ONBUILD RUN git pull https://github.com/crossgovernmentservices/csl-learner-
plan-viewer.git && pip install -r
/home/dev/learner_plan_viewer/requirements/dev.txt  
EXPOSE 8000  
CMD ["./run_prod.sh", "8000"]

