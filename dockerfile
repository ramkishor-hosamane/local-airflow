# Use an official Python runtime as the base image
FROM apache/airflow

# Copy custom configuration files
COPY airflow.cfg /opt/airflow/airflow.cfg

# Initialize the Airflow database
RUN airflow db init

# Create the default user
RUN airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Expose the required Airflow ports
EXPOSE 8080

# Start the Airflow webserver
CMD ["webserver"]