FROM python:3.9-slim

WORKDIR /app

COPY upload_s3.py .

COPY movies.csv series.csv /app/

RUN pip install boto3 pandas

CMD ["python", "upload_s3.py"]