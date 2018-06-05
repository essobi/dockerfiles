FROM tensorflow/tensorflow:1.1.0 as trainer  
  
COPY ./images /images  
COPY ./tf /tf  
RUN sed -i 's/\r//' /tf/*.*  
  
WORKDIR /tf  
RUN python -m retrain --how_many_training_steps=10
--bottleneck_dir=tf_files/bottlenecks --model_dir=tf_files/models/
--summaries_dir=tf_files/training_summaries/bowling
--output_graph=tf_files/retrained_graph.pb
--output_labels=tf_files/retrained_labels.txt --image_dir=/images  
  
FROM tensorflow/tensorflow:1.1.0 as flask  
  
RUN pip install Flask  
  
COPY \--from=trainer /tf/tf_files/retrained_labels.txt
/tf/tf_files/retrained_labels.txt  
COPY \--from=trainer /tf/tf_files/retrained_graph.pb
/tf/tf_files/retrained_graph.pb  
  
COPY ./code /code  
RUN sed -i 's/\r//' /code/*.*  
  
WORKDIR /code  
EXPOSE 5000  
CMD ["python", "app.py"]

